import requests
from chapter import Chapter
from save import load_save, update_save
from config import load_config
from bs4 import BeautifulSoup

config = load_config()
urls = config['urls']

save = load_save()

new_release = False
for url in urls:
    # Convert HTML to soup.
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')

    # Get chapter information from soup.
    ch = Chapter(soup)

    # Check and see if the chapter is more recent than what was last saved.
    manga = ch.manga_title.lower()
    if manga not in save or save[manga] < ch.num:
        print('New chapter.')
        save[manga] = ch.num
        new_release = True

if new_release:
    update_save(save)
