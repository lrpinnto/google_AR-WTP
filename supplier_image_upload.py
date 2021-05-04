#!/usr/bin/env python3
import requests
import os
# This example shows how a file can be uploaded using
# The Python Requests module

url = "http://localhost/upload/"
path = "./supplier-data/images/"
for files in os.listdir(path):
    if files.endswith(".jpeg"):
        with open(path + files, 'rb') as opened:
            r = requests.post(url, files={'file': opened})
