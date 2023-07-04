from fbchat import Client
from fbchat.models import Message
from credentials import *

CLIENT = Client(
        SENDER_FACEBOOK_USERNAME,
        SENDER_FACEBOOK_PASSWORD)


def send_message(message, user):
    CLIENT.send(Message(text=message), thread_id=user.uid)
    # client.logout()
def send_photo(photo_path , user):
    CLIENT.sendLocalImage(photo_path , thread_id=user.uid)

def send_video(video_path, user):
        CLIENT.sendLocalImage(video_path, thread_id=user.uid)


def send_audio(audio_path, user):
    CLIENT.sendLocalImage(audio_path, thread_id=user.uid)

def get_friends():
    users = CLIENT.fetchThreadList()
    detailed_users = [
        list(CLIENT.fetchThreadInfo(user.uid).values())[0] for user in users
    ]

    return detailed_users
