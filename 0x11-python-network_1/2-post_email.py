#!/usr/bin/python3
""" sends a post request"""
from urllib import request, parse
from sys import argv
if __name__ == "__main__":
    values = {"email": argv[2]}
    data = parse.urlencode(values)
    data = data.encode('utf8')
    url = argv[1]
    req = request.Request(url, data)
    with request.urlopen(req) as response:
        print(response.read().decode("utf8"))
