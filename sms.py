import os
from twilio.rest import Client
from credentials import ACCOUNT_SID, AUTH_TOKEN


client = Client(ACCOUNT_SID, AUTH_TOKEN)


def send_sms(sender, receiver, message ):
    client.messages.create(
            from_=sender,
            to=receiver,
            body=message,
    )
    print("[OK] SMS sent to SIM")
def send_mms(sender, receiver, message, media_urls=[]):
    client.messages.create(
            from_=sender,
            to=receiver,
            body=message,
            media_url=media_urls
    )
    print("[OK] MMS sent to SIM")

