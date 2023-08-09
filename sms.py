from config import load_config
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
import requests
import json

config = load_config()

def send_notification(chapter):
    """Sends a SMS using the details of the given chapter."""
    twilio_sid = config["twilio_sid"]
    twilio_access_token = config["twilio_access_token"]
    twilio_number = config["twilio_number"]
    personal_number = config["personal_number"]

    try:
        client = Client(twilio_sid, twilio_access_token)
        message = client.messages.create(
            to=personal_number,
            from_=twilio_number,
            body=str(chapter)
        )
    except TwilioRestException as err:
        raise Exception(res.text)
