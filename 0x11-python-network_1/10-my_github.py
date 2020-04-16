#!/usr/bin/python3
""" My GitHub """
import requests
from requests.auth import HTTPBasicAuth
import sys


if __name__ == "__main__":
    user = sys.argv[1]
    token = sys.argv[2]
    req = requests.get('https://api.github.com/user'
                       auth=HTTPBasicAuth(user, token))
    req_dict = req.json()
    print(req_dict.get('id'))
