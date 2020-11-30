import logger
import json

def load_save():
    """Loads the dictionary from the save file that maps mangas to latest chapter numbers."""
    try:
        with open('save.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def update_save(d):
    """Saves the given dictionary to the save file."""
    with open('save.json', 'w') as f:
        json.dump(d, f, indent=4)
