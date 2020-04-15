#!/usr/bin/python3
import urllib.request
""" What's my status """

if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as request:
        html = request.read()
        print('Body response:\n\
\t- type: {}\n\
\t- content: {}\n\
\t- utf8 content: {}'.format(type(html), html, html.decode('utf-8')))
