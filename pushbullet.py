from config import load_config
import requests
import json

config = load_config()

def send_push(chapter):
    """Sends a push using the details of the given chapter."""
    access_token = config['access_token']
    message = {
            'type': 'note', 
            'title': 'New Chapter',
            'body': str(chapter)
            }

    res = requests.post('https://api.pushbullet.com/v2/pushes',
            data=json.dumps(message),
            headers={
                'Access-Token': access_token,
                'Content-Type': 'application/json'
                })
    
    if res.status_code != 200:
        raise ConnectionError(res.text)
