#!/usr/bin/env python3

import requests
import os

url = "http://localhost/upload/"
dir = "/home/<studentID>/supplier-data/images"
images = os.listdir(dir)

for image in images:
    image_path = os.path.join(dir, image)
    with open(image_path, 'rb') as img:
        r = requests.post(url, files={'file': img})
