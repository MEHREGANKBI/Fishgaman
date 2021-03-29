#!/usr/bin/env python3

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import numpy as np
import subprocess
from usps import conf_dict

#given a string, turn it into an image with white background. Text color is black.
def text2img(stringList):
    img = Image.new('RGB', (300, 150), (255, 255, 255))
    drawer = ImageDraw.Draw(img)
    font = ImageFont.truetype(conf_dict['font_path'], 14)
    drawer.text((20, 20), '\n\n'.join(stringList), fill=(0, 0, 0), font = font)
    return np.array(img)
    
#given a numpy array of an img, patch it on a the top right corner of another image, and set that another image as Desktop background
def img2bg(imgArray):
    image = np.array(Image.open(conf_dict['pre_wallpaper_path']))
    image[50:200, 1040:1340, :] = imgArray[:,:,:]
    image = Image.fromarray(image)
    image.save(conf_dict['edited_wallpaper_path'])
    return conf_dict['cwd'] + '/' + conf_dict['edited_wallpaper_path']
    
#given an image file set it as wallpaper. 
def setwp(imageFile):
    subprocess.run(['gsettings', 'set', 'org.gnome.desktop.background', 'picture-uri', imageFile])
