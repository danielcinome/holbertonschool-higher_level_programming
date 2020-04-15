#!/usr/bin/python3
import urllib.request
import sys
""" What's my status """

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    values = {'email': email}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        res_data = response.read().decode('utf-8')
    print(res_data)
