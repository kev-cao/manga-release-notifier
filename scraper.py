import requests

def save_html(html, path):
    """Writes an HTML file to persistent storage."""
    with open(path, 'wb') as f:
        f.write(html)

def open_html(path):
    """Returns the contents of an HTML file as a string."""
    with open(path, 'rb') as f:
        return f.read()

url = 'https://manganelo.com/chapter/karakai_jouzu_no_takagisan/chapter_136'
r = requests.get(url)

html = r.content
save_html(html, './manga.html')

