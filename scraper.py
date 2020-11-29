import requests
from chapter import Chapter
from urls_reader import get_urls
from bs4 import BeautifulSoup

urls = get_urls()

for url in urls:
    # Convert HTML to soup.
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')

    # Get chapter information from soup.
    ch = Chapter(soup)
    print(ch)
