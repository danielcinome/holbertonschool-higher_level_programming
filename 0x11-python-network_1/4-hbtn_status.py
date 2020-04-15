#!/usr/bin/python3
""" What's my status? """
import requests


if __name__ == "__main__":
    req = requests.get('https://intranet.hbtn.io/status')
    print('Body response:\n\
\t- type: {}\n\
\t- content: {}'.format(type(req.encoding), req.content.decode('utf-8')))
