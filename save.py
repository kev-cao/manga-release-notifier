import json

def load_save():
    """Loads the dictionary from the save file that maps mangas to latest chapter numbers."""
    try:
        with open('save.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError("Make sure to run init.py before starting the scraper.")

def update_save(d):
    """Saves the given dictionary to the save file."""
    with open('save.json', 'w') as f:
        json.dump(d, f, indent=4)
