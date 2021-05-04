#!/usr/bin/env python3
from PIL import Image
import os
#converts all images, saves them in the same path
directory = "./supplier-data/images/"
for files in os.listdir(directory):
    if files.endswith(".tiff"):
        name = files.split(".")[0] + ".jpeg"
        im = Image.open(directory + files)
        im_conv = im.convert("RGB")
        im_conv.resize((600, 400)).save(directory + name, "JPEG")
