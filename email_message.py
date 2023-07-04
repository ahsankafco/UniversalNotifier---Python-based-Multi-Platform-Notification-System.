import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from credentials import *


def send_email_text(subj,bo,receiver):
    subject = subj
    body = bo
    RECIEVER_EMAIL = receiver

    message = MIMEMultipart()
    message["From"] = SENDER_EMAIL_USERNAME
    message["To"] = RECIEVER_EMAIL
    message["Subject"] = subject

    message.attach(MIMEText(body, "plain"))

    text = message.as_string()

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(SENDER_EMAIL_USERNAME, SENDER_EMAIL_PASSWORD)
        server.sendmail(SENDER_EMAIL_USERNAME, RECIEVER_EMAIL_USERNAME, text)


def send_email_media(subj, bo, file,receiver):
    subject = subj
    body = bo
    RECIEVER_EMAIL=receiver
    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = SENDER_EMAIL_USERNAME
    message["To"] = RECIEVER_EMAIL
    message["Subject"] = subject

    # Add body to email
    message.attach(MIMEText(body, "plain"))
    filename = file  # In same directory as script

    # Open PDF file in binary mode
    with open(filename, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email
    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )

    # Add attachment to message and convert message to string
    message.attach(part)
    text = message.as_string()

    # Log in to server using secure context and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(SENDER_EMAIL_USERNAME, SENDER_EMAIL_PASSWORD)
        server.sendmail(SENDER_EMAIL_USERNAME, RECIEVER_EMAIL, text)