#! /usr/bin/env python3

import os
import requests

feedback_path = '/data/feedback'

feedbacks = os.listdir(feedback_path)

result = {}

for feedback in feedbacks:
   with open (feedback_path + '/' + feedback) as file:
      data = [line.strip() for line in file.readlines()]
      result = {"title": data[0], "name": data[1], "date": data[2], "feedback": data[3]}
   response = requests.post('http://<external_IP_web_server>/feedback/', data=result)
   response.raise_for_status()
