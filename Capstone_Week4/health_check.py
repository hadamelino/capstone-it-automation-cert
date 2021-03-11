#!/usr/bin/env python3

import psutil
import emails
import socket

def cpu_check():
    cpu_usage = psutil.cpu_percent(1)
    return not cpu_usage > 80

def disk_available():
    disk_usage = psutil.disk_usage('/')
    return not disk_usage.percent > 20

def avail_mem():
    avail = psutil.virtual_memory().available
    avail_MB = avail / 1024 ** 2 #Convert to MB
    return not avail_MB > 500

def hostname_check():
    local_host_ip = socket.gethostbyname('localhost')
    return not local_host_ip == "127.0.0.1"

def generate_email_content(subject_line):
    sender = "automation@example.com"
    recipient = "<studentID>@example.com"
    subject = subject_line
    body = "Please check your system and resolve the issue as soon as possible."
    message = emails.generate_warning_email(sender, recipient, subject_line, body)
    emails.send_email(message)

if cpu_check():
    subject_line = "Error - CPU usage is over 80%"
    generate_email_content(subject_line)

if disk_available():
    subject_line = "Error - Available disk space is less than 20%"
    generate_email_content(subject_line)

if avail_mem():
    subject_line = "Error - Available memory is less than 500MB"
    generate_email_content(subject_line)

if hostname_check():
    subject_line = "Error - localhost cannot be resolved to 127.0.0.1"
    generate_email_content(subject_line)
