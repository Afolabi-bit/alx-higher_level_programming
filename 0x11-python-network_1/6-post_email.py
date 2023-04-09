#!/usr/bin/python3
"""
   Sends a POST request to a given URL with a given email
   Displays the body of the response.
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = {"email": sys.argv[2]}

    r = requests.post(url, data=email)
    print(r.text)
