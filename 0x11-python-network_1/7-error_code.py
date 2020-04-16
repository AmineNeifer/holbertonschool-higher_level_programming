#!/usr/bin/python3
"""
sends a request to the URL and displays the body of the response.
"""
import sys
import requests
if __name__ == "__main__":
    r = requests.get(sys.argv[1]).text
    if r[0:5] == "Error":
        print("Error code:", r[6:])
    else:
        print(r)
