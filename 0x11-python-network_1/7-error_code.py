#!/usr/bin/python3
""" Error code #1 """
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    req = requests.get(url)
    try:
        req.raise_for_status()
        print(req.text)
    except:
        print('Error code: {}'.format(req.status_code))
