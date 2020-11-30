# Manga Release Notifier
Sends a push notification every time a new chapter of a followed manga is released.

## Context
Wanted to give web-scraping a try, so decided to make this project. It's a bit redundant, since any manga website will send you email notifications if you sign up for an account with them. But this method doesn't require you to give out your email to the advertisers that websites inevitably send your contact info to, and it's cooler.

The program mainly uses the `requests` and `bs4` Python libraries to check the website for a new chapter release, and if it detects one, it sends a push notification to your device with Pushbullet. Oh, you'll need to download Pushbullet.

I largely wanted to spend time focusing on properly organizing my code and separating concerns, as my last project showed me that it was an area of weakness for me. Overall, I think I did a much better job than I usually do, but the `setup.py` file could definitely be cleaned up more.

## How to Use
This program uses Pushbullet and its API to send push notifications, so you will need to set up an account on Pushbullet. Once you are there, copy down your Pushbullet access token from [account settings](https://www.pushbullet.com/#settings) (you need to keep this secret).

From there, in the repo directory, run
```
python setup.py
```

Follow the instructions there. At the moment, the program only supports the Manganelo website, but I plan on adding a bit more support to similar sites like Managakalot.

That sets up the `config.json` file. Next, you will need to set up a way to repeatedly run `scraper.py`. If you're on Linux, I recommend using cron jobs. I set up a bash script like so to run the scraper:
```bash
#!/bin/bash
cd $REPO_DIRECTORY_HERE
if [[ -f "config.json" ]]; then
  source bin/activate # Only have this line if you are using virtual environments.
  python scraper.py
fi
```

Then, in the crontab, I have the script set to run every 2 hours, but you can change this to your liking of course ([Cron Tutorial](https://phoenixnap.com/kb/set-up-cron-job-linux)).
```bash
# Manga Notifier Script Job
0 */2 * * * $SCRIPT_LOCATION
```

Alternatively, if you don't want to set up scheduled tasks, you can use a loop to stop the script from terminating. If you check `scraper.py`, you will find a comment detailing where you should insert the loop. Also make sure to import the `time` library. There, create a while loop that runs indefinitely and push everything under that line into the while loop body. Then simply add a sleep delay in seconds equal to however frequently you want the scraper to check the website.
```python
import time
while True:
  # Other code.
  time.sleep(2 * 60 * 60) # Sleep for 2 hours.
```
