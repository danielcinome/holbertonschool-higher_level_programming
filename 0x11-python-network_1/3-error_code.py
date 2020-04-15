#!/usr/bin/python3
import urllib.request
import sys
"""  Error code #0 """

if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as request:
            val = request.read().decode('utf-8')
            print(val)
    except urllib.error.HTTPError as e_http:
        print('Error code: {}'.format(e_http.code))
