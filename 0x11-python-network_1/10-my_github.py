#!/usr/bin/python3
"""
retrieve id from profile
"""
import requests
from sys import argv
if __name__ == "__main__":
    r = requests.get('https://api.github.com/user', auth=(argv[1], argv[2]))
    try:
        print(r.json()["id"])
    except KeyError:
        print("None")
