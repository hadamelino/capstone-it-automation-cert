#!/usr/bin/env python3

from PIL import Image
import os

dir = '/home/<studentID>/supplier-data/images'
image_list = os.listdir(dir)

for file in image_list:
   file_name = file.split('.')[0]
   file_path = os.path.join(dir, file)
   if file.endswith('.tiff'):
      img = Image.open(file_path)
      rgb_img = img.convert("RGB")
      rgb_img = rgb_img.resize((600,400))
      rgb_img.save(dir + '/' + file_name + '.jpeg')
      os.remove(file_path)
