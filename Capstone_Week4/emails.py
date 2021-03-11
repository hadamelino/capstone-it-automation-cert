#!/usr/bin/env python3

from email.message import EmailMessage
import smtplib
import mimetypes
import os

def generate_email(sender, recipient, subject, body, attachment_path):
    """Creates an email with an attachment."""
    #Add header email
    message = EmailMessage()
    message['From'] = sender
    message['To'] = recipient
    message['Subject'] = subject
    message.set_content(body)

    #Add attachment email
    mime_type, _ = mimetypes.guess_type(attachment_path)
    mime_type, mime_subtype = mime_type.split('/', 1)
    with open(attachment_path, 'rb') as attch:
        message.add_attachment(attch.read(), maintype=mime_type, subtype=mime_subtype, filename=os.path.basename(attachment_path))

    return message

def generate_warning_email(sender, recipient, subject, body):
    """Creates email for health_checks"""
    #Add header email
    message = EmailMessage()
    message['From'] = sender
    message['To'] = recipient
    message['Subject'] = subject
    message.set_content(body)

    return message

def send_email(message):
    """Sends the message to the configured STMP server."""
    mail_server = smtplib.SMTP('localhost')
    mail_server.send_message(message)
    mail_server.quit()
