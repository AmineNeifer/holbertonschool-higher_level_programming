#!/usr/bin/python3
""" display the value of X-Request-Id found in header"""
import sys
from urllib import request
if __name__ == "__main__":
    req = request.Request(sys.argv[1])
    with request.urlopen(req) as res:
        print(res.getheader("X-Request-Id"))
