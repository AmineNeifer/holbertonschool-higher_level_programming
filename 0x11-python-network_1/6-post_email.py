#!/usr/bin/python3
"""
send post request using requests module.
"""
import requests
if __name__ == "__main__":
    url = "http://0.0.0.0:5000/post_email"
    myobj = {"email": "hr@holbertonschool.com"}
    print(requests.post(url, data=myobj).text)
