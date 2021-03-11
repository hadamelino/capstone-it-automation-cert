#!/usr/bin/env python3

from datetime import datetime
import os
import reports
import run
import emails

def fetch_data(data):
    summary = []
    for content in data:
        summary.append("name: {}<br/>weight: {} lbs".format(content['name'], content['weight']))
    info = "<br/><br/>".join(summary)
    return info

if __name__ == "__main__":

    #Generate pdf for attachment
    list_of_dict = run.get_dict()
    pdf_content = fetch_data(list_of_dict)
    attachment_path = "/tmp/processed.pdf"
    date_now = datetime.now().strftime("%b %d, %Y")
    title = "Processed Update on" + date_now
    reports.generate_report(attachment_path, title, pdf_content)

    #Send email with header and attachment
    sender = "automation@example.com"
    recipient = "<studentID>@example.com"
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    message = emails.generate_email(sender, recipient, subject, body, attachment_path)
    emails.send_email(message)
