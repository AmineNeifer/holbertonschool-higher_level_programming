#!/usr/bin/python3
"""
sends a request to the URL and displays the body of the response.
"""
import sys
import requests
if __name__ == "__main__":
    print(requests.get(sys.argv[1]).status_code)
