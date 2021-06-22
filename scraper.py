import requests
from logger import logger
from chapter import Chapter
from save import load_save, update_save
from config import load_config
from bs4 import BeautifulSoup
from pushbullet import send_push

config = load_config()
urls = config['urls']

save = load_save()

logger.info("Running scraper.")

# If you do not wish to use a task scheduler and want this program
# to run indefinitely instead, start the while loop below
# this comment. See README for more details.
need_to_save = False
for url in urls:
    # Convert HTML to soup.
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')

    try: 
        # Get chapter information from soup.
        ch = Chapter(soup)

        # Check and see if the chapter is more recent than what was last saved.
        manga = ch.manga_title.lower()
        ch.fetch_chapter_details(save[manga])
        if manga not in save or save[manga] < ch.num:
            try:
                if manga in save:
                    logger.info(f'Sent push for {ch.manga_title}.')
                    send_push(ch)

                save[manga] = ch.num
                need_to_save = True
            except ConnectionError as e:
                logger.error(e)
    except ValueError as e:
        logger.error(e)

if need_to_save:
    update_save(save)
