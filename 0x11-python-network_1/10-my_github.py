#!/usr/bin/python3
""" My GitHub """
import requests
import sys


if __name__ == "__main__":
    user = sys.argv[1]
    token = sys.argv[2]
    req = requests.get('https://api.github.com/user', auth=(user, token))
    req_dict = req.json()
    print(req_dict.get('id'))
