from facebook_message import send_message as send_facebook_message, get_friends
from facebook_message import send_photo as send_facebook_photo, get_friends
from facebook_message import send_video as send_facebook_video, get_friends
from facebook_message import send_audio as send_facebook_audio, get_friends
from instagram_message import send_message as insta_message_for_text
from sms import send_sms as send_sms_message
from sms import send_mms as send_mms_message
from email_message import send_email_text as send_mail_for_text
from email_message import send_email_media as send_mail_for_media


def send_message_for_sms():
    sender = str(input("Number From: "))
    receiver = str(input("Number To: "))
    message = str(input("Type Message: "))
    send_sms_message(sender, receiver, message)


def send_media_for_mms():
    sender = str(input("Number From: "))
    receiver = str(input("Number To: "))
    message = str(input("Type Message: "))
    media_urls = str(input("share urls: "))
    send_mms_message(sender, receiver, message, media_urls)


def send_message_for_facebook():
    print("Select your friend: ")
    friends = get_friends()
    friend_index = 1
    friends_hashmap = dict()
    for friend in friends:
        friends_hashmap[friend_index] = friend
        print(f"[{friend_index}] {friend.name}")
        friend_index += 1

    friend_option = int(input())
    user = friends_hashmap[friend_option]

    message = str(input("Enter text: "))
    send_facebook_message(message, user)


def send_message_for_photo():
    print("Select your friend: ")
    friends = get_friends()
    friend_index = 1
    friends_hashmap = dict()
    for friend in friends:
        friends_hashmap[friend_index] = friend
        print(f"[{friend_index}] {friend.name}")
        friend_index += 1

    friend_option = int(input())
    user = friends_hashmap[friend_option]

    photo_path = str(input("photo name/Directory: "))
    send_facebook_photo(photo_path, user)


def send_message_for_video():
    print("Select your friend: ")
    friends = get_friends()
    friend_index = 1
    friends_hashmap = dict()
    for friend in friends:
        friends_hashmap[friend_index] = friend
        print(f"[{friend_index}] {friend.name}")
        friend_index += 1

    friend_option = int(input())
    user = friends_hashmap[friend_option]

    video_path = str(input("video name/Directory: "))
    send_facebook_video(video_path, user)


def send_message_for_audio():
    print("Select your friend: ")
    friends = get_friends()
    friend_index = 1
    friends_hashmap = dict()
    for friend in friends:
        friends_hashmap[friend_index] = friend
        print(f"[{friend_index}] {friend.name}")
        friend_index += 1

    friend_option = int(input())
    user = friends_hashmap[friend_option]

    audio_path = str(input("Audio name/Directory: "))
    send_facebook_audio(audio_path, user)

def send_message_for_insta():
    message=str(input("Type Message: "))
    RECIEVER_ID= str(input("Enter Instagram Receiver ID: "))
    insta_message_for_text(message,RECIEVER_ID)

def send_mail_for_at():
    subj = str(input("Enter Subject: "))
    bo = str(input("Enter Body: "))
    receiver = str(input("Enter Receiver Email Address: "))
    send_mail_for_text(subj,bo,receiver)

def send_mail_for_m():
    subj = str(input("Enter Subject: "))
    bo = str(input("Enter Body: "))
    receiver = str(input("Enter Receiver Email Address: "))
    file = str(input("Enter Media name or Directory: "))
    send_mail_for_media(subj,bo,file,receiver)

def print_medium():
    print("Select option: ")
    print("[1] facebook")
    print("[2] instagram")
    print("[3] email")
    print("[4] sms/mms")


def print_message_type_for_facebook():
    print("Select Notification Type: ")
    print("[1] Text")
    print("[2] Image")
    print("[3] Video")
    print("[4] Audio")

def print_message_type_for_email():
    print("Select Notification Type: ")
    print("[1] Text")
    print("[2] Image")
    print("[3] Video")
    print("[4] Audio")
    print("[5] PDF")


def print_message_type_for_sim():
    print("[1] sms")
    print("[2] mms")


def app():
    facebook = 1
    instagram = 2
    email = 3
    sms = 4

    text = 1
    image = 2
    video = 3
    audio = 4
    pdf = 5

    sim_sms = 1
    sim_mms = 2

    continue_program = True
    while continue_program:
        print_medium()
        option = int(input())
        if option == facebook:
            print_message_type_for_facebook()
            message_type = int(input())
            if message_type == text:
                send_message_for_facebook()
            elif message_type == image:
                send_message_for_photo()
            elif message_type == video:
                send_message_for_video()
            elif message_type == audio:
                send_message_for_audio()

        if option == sms:
            print_message_type_for_sim()
            message_type = int(input())
            if message_type == sim_sms:
                send_message_for_sms()
            elif message_type == sim_mms:
                send_media_for_mms()

        if option == email:
            print_message_type_for_email()
            email_type = int(input())
            if email_type == text:
                send_mail_for_at()
            elif email_type == image:
                send_mail_for_m()
            elif email_type == video:
                send_mail_for_m()
            elif email_type == audio:
                send_mail_for_m()
            elif email_type == pdf:
                send_mail_for_m()
        if option == instagram:
            send_message_for_insta()



        print("Do you want to continue?")
        user_continue_state = str(input())

        continue_program = user_continue_state == "y" or user_continue_state == "Y"

    print("Thank you for using our app")


if __name__ == "__main__":
    app()
