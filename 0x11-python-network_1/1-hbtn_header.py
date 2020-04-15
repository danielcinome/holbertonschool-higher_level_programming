#!/usr/bin/python3
import urllib.request
import sys
""" What's my status """

if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(req) as request:
        head = request.info()
    head_dic = dict(head)
    print(head_dic['X-Request-Id'])
