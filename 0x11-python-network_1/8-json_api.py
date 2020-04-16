#!/usr/bin/python3
""" Search API """
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        letter = {'q': sys.argv[1]}
    else:
        letter = {'q': ''}
    req = requests.post("http://0.0.0.0:5000/search_user", data=letter)
    try:
        req_dict = req.json()
        print('[{}] {}'.format(req_dict.get('id'), req_dict.get('name')))
    except:
        print('No result')
