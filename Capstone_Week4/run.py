#!/usr/bin/env python3

import os
import requests

def get_dict():
    dir = "/home/<studentID>/supplier-data/descriptions"
    descs = os.listdir(dir)
    all_desc = []

    for desc in descs:
        desc_path = os.path.join(dir, desc)
        with open(desc_path) as file:
            data = [line.strip() for line in file.readlines()]
            weight = int(data[1].strip(' lbs'))
            try:
                file_name = desc.strip('.txt')
            except:
                print('found a file without .txt extension')
            all_desc.append({'name': data[0], 'weight': weight, 'description': data[2], 'image_name': file_name + '.jpeg'})
    return all_desc

def post_dict(all_desc, url):
    for desc in all_desc:
        r = requests.post(url, data=desc)
        r.raise_for_status()
    print("Done post data")

if __name__ == "__main__":
    url = "http://localhost/fruits/"
    all_desc = get_dict()
    print(all_desc)
    post_dict(all_desc, url)
