from PIL import Image
import os

source_path = '/home/<student ID>/images'

dir = os.listdir(source_path)

for file in dir:
    dest = '/opt/icons'
    try:
        if not file.endswith('.jpg'):
            img = Image.open(dir)
            img.rotate(270).resize((128, 128)).convert('RGB')
            img.save(dest + '.jpg')
    except:
        continue
