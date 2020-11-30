import requests
from chapter import Chapter
from config import load_config, save_config
from bs4 import BeautifulSoup
import os

try:
    config = load_config()
except FileNotFoundError:
    config = {}

##############################
######### Functions ##########
##############################
def init():
    """Begins the initialization of the config."""
    clear_term()
    global config
    config = {}

    # Get access token.
    token = get_access_token()

    # Get manga URLs.
    config['urls'] = []
    get_manga_urls()

def get_access_token():
    """Prompts user for a new access token and updates it in the config."""
    print("Please provide your Pushbullet Access Token. You can find instructions on how to find the token here: https://docs.pushbullet.com/v1/#http")
    token = input('Token: ')
    change_access_token(token)

def get_manga_urls():
    """Adds a sequence of URLs to the config."""
    print("Enter the URLs of the chapter list of a manga you would like to follow (example: https://manganelo.com/manga/shigatsu_wa_kimi_no_uso).")
    while True:
        url = get_url()
        if url:
            add_manga_url(url)
        else:
            break

def get_url():
    """Prompts user for a URL. If the user cancels, returns none."""
    url = input("URL (enter 'q' to cancel): ")
    if url == 'q':
        return None
    return url

def add_manga():
    """Prompts user for and adds manga."""
    print("Enter the URL of the chapter list of the manga you would like to follow.")
    url = get_url()
    if url:
        add_manga_url(url)

def display_manga():
    """Displays all of the followed manga."""
    global config
    urls = config['urls']

    print("Followed Manga\n--------------")
    for idx, url in enumerate(urls):
        ch = convert_url_to_chapter(url)
        print(f"{idx}. {ch.manga_title}")

def remove_manga():
    """Displays available manga to user and prompts them for removal."""
    display_manga()
    print()
    try:
        idx = int(input("Enter the number of the manga you would like removed: "))
        remove_manga_url(idx)
    except ValueError:
        print("Invalid choice.")

def convert_url_to_chapter(url):
    """Converts a URL to a chapter."""
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')
    return Chapter(soup)

def add_manga_url(url):
    """Adds a manga with the given URL to the config."""
    try:
        convert_url_to_chapter(url)

        # If it gets to here, the url is valid.
        global config
        if url in config['urls']:
            print("You are already following this manga.")
        else:
            config['urls'].append(url)
    except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError, ValueError):
        print('Could not add manga. Make sure the link leads to the chapter list of the manga.')

def remove_manga_url(idx):
    """Removes the manga at the given index from the config."""
    try:
        global config
        del config['urls'][idx]
    except IndexError:
        print('That manga does not exist in the config.')

def change_access_token(token):
    """Changes the Pushbullet Access Token stored in the config."""
    global config
    config['access_token'] = token

def clear_term():
    """Clears the terminal."""
    os.system('cls' if os.name == 'nt' else 'clear') 

##############################
####### Script Start #########
##############################
clear_term()

menu = {
        1: {'text': "Reset Config", 'func': init},
        2: {'text': "Add Manga", 'func': add_manga},
        3: {'text': "Remove Manga", 'func': remove_manga},
        4: {'text': "Change Pushbullet Access Token", 'func': get_access_token},
        5: {'text': "Save"},
        6: {'text': "Save and Quit"},
        7: {'text': "Quit without Saving"}
        }

if len(config) == 0:
    init()
    clear_term()

while True:
    try:
        for key in menu:
            text = menu[key]['text']
            print(f"{key}. {text}")

        choice = int(input("Menu choice: "))

        if 'func' in menu[choice]:
            menu[choice]['func']()
        else:
            if choice <= 6:
                save_config(config)
            if choice >= 6:
                break
    except (ValueError, KeyError):
        print("Not a valid choice. Please try again.")

    input("Press Enter to continue...")
    clear_term()
