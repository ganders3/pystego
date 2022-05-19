#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#from scipy import misc
#import imageio

import os
import random
from PIL import Image, ImageStat

# Change directory
os.chdir("./pystego")

img = Image.open("cheese.jpg")
#img.show()

#pix = img.load()

imgRgb = img.convert("RGB")

width, height = imgRgb.size
x1, x2 = [int(random.uniform(0, width)) for i in range(0,2)]
y1, y2 = [int(random.uniform(0, height)) for i in range(0,2)]


for i in range(min(x1, x2), max(x1, x2)):
    for j in range(min(y1, y2), max(y1, y2)):
        imgRgb.putpixel((i, j), (255, 255, 255))
#    print(i)

imgRgb.show()






stat = ImageStat.Stat(img)



r, g, b = imgRgb.getpixel((1, 1))

#pix = img.load()