import requests
import re
from bs4 import BeautifulSoup

def save_html(html, path):
    """Writes an HTML file to persistent storage."""
    with open(path, 'wb') as f:
        f.write(html)

def open_html(path):
    """Returns the contents of an HTML file as a string."""
    with open(path, 'rb') as f:
        return f.read()

# Temporary URL to parse.
url = 'https://manganelo.com/manga/karakai_jouzu_no_takagisan'
r = requests.get(url)

# Convert HTML raw text to soup.
soup = BeautifulSoup(r.content, 'html.parser')

# Get most recent chapter number.
chapter_list = soup.select_one('.panel-story-chapter-list')
recent_chapter = chapter_list.find('li', class_='a-h')
chapter_title = recent_chapter.a['title']

pattern = r'chapter\s*(\d*):*'
match = re.search(pattern, chapter_title, re.IGNORECASE)

if match:
    chapter_num = match.group(1)
