#!/usr/bin/python3
""" sends a post request"""
from urllib import request, parse
from sys import argv
if __name__ == "__main__":
    params = {"email": argv[2]}
    querystring = parse.urlencode(params)
    url = sys.argv[1] + "?" + querystring
    with request.urlopen(url) as resp:
        print(resp)
