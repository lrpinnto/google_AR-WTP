#! /usr/bin/env python3
import os
import requests

fruits = {}
#"name", "weight", "description", "image_name"
path = "./supplier-data/descriptions/"
img_path = "./supplier-data/images/"
for file in os.listdir("./supplier-data/descriptions"):
    with open(path + file) as f:
        count=1
        for ln in f: #should rewrite this to go 1,2,3 instead of checking if the information matches. so 1 name 2 weight 3 description
            line = ln.strip()
            if count==1:
                fruits["name"] = line
                count+=1
            elif count==2 and "lbs" in line:
                weight_2_int = int(line.split()[0])
                fruits["weight"] = weight_2_int
                count+=1
            elif count == 3:
                fruits["description"] = line
                count=1
            else:
                raise NameError("else case")

        filename = file.split(".")
        imgname = filename[0] + ".jpeg"
        for fle in os.listdir("./supplier-data/images"):
            if fle == imgname:
                fruits["image_name"] = imgname
        response = requests.post("http://<ip>/fruits/", json=fruits)
        fruits.clear()
