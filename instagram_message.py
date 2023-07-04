from instagrapi import Client
from credentials import *


def send_message(message):
    client = Client()
    client.login(
        SENDER_INSTAGRAM_USERNAME,
        SENDER_INSTAGRAM_PASSWORD)
    print("[OK] Logged in to instagram")
    dm_reciever_uid = client.user_id_from_username(
        RECIEVER_INSTAGRAM_USERNAME)

    # send text message
    client.direct_send(message, [dm_reciever_uid])
    print("[OK] Sent text message")



#send photo
#image_url = "https://scontent-dfw5-1.cdninstagram.com/v/t51.2885-15/284873896_1400624793744591_8579849805855027852_n.jpg?stp=dst-jpg_e0_p480x480&cb=9ad74b5e-b94cae63&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_cat=103&_nc_ohc=acX5FytTwckAX92QFVs&edm=ABJHkxYAAAAA&ccb=7-5&ig_cache_key=Mjg1MDQxMzQ5NTEzMDMyMjQ2OA%3D%3D.2-ccb7-5&oh=00_AT86LHnYY0qX5NsTU14u1yDbAOi8x6ZGq7s1U9GNQeopAA&oe=629C5FEE&_nc_sid=fa978c"
#photo_path = client.photo_download(client.media_pk_from_url(image_url))
#print("photo_path", photo_path) 
#client.direct_send_photo(photo_path, [dm_reciever_uid])
#print("Sent image")
