import logger
import json

def load_config():
    """Loads the configuration file for the scraper and returns it."""
    try:
        with open('config.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError("Make sure to run init.py before running the scraper.")

def save_config(config):
    """Updates the configuration file with the given config."""
    with open('config.json', 'w') as f:
        json.dump(config, f, indent=4)
