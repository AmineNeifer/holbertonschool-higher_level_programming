#!/usr/bin/python3
"""
retrieve id from profile
"""
import requests
import sys
if __name__ == "__main__":
    r = requests.get('https://api.github.com/user', auth=(sys.argv[1], sys.argv[2]))
    try:
        print(r.json()["id"])
    except KeyError:
        print("None")
