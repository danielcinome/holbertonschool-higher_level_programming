#!/usr/bin/python3
""" POST an email #1 """
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data_post = {'email': email}
    req = requests.post(url, data=data_post)
    print(req.text)
