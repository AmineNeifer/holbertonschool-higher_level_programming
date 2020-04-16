#!/usr/bin/python3
"""
display the body of the respons.
if there's a problem, display error code.
"""
from urllib import request
import urllib.error
import sys
if __name__ == "__main__":
    req = request.Request(sys.argv[1])
    try:
        with request.urlopen(req) as res:
            print(res.read().decode("utf8"))
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
