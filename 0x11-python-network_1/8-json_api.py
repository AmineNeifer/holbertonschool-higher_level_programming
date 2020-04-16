#!/usr/bin/python3
"""
takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user.
"""
import sys
import requests
if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    try:
        myobj = {"q": sys.argv[1]}
    except IndexError:
        myobj = {"q": ""}
    r = requests.post(url, data=myobj)
    try:
        print("[{}] {}".format(r.json()['id'], r.json()['name']))
    except KeyError:
        print("No result")
