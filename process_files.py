!/usr/bin/env python3

import os, glob
import requests
import json

os.chdir("/data/feedback")

for review in glob.glob("*.txt"):
   with open(review, "r") as in_file:
       d = {}
       keys = ["title", "name", "date", "feedback"]
       count = 0
       for line in in_file:
           d[keys[count]] = line.rstrip("\n")
           count += 1
       print(d)
       response = requests.post("http://<external-IP/feedback/", data=d)
       print(response.status_code)
