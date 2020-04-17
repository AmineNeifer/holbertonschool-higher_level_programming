#!/usr/bin/python3
"""
displays the value of variable in a response header.
"""
import requests
import sys
if __name__ == "__main__":
    try:
        print(requests.get(sys.argv[1]).headers["X-Request-Id"])
    except:
        pass
