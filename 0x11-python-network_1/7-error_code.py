#!/usr/bin/python3
"""
sends a request to the URL and displays the body of the response.
"""
import sys
import requests
if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    if r.status_code != 200:
        print("Error code:", r.status_code)
    else:
        print(r.text)
