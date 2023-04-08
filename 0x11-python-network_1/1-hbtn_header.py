#!/usr/bin/python3
"""
   Takes in a URL, sends a request to it
   Displays the X-Request-Id header variable found in the header
"""
import sys
import urllib.request


if __name__ == "__main__":
    link = sys.argv[1]

    req = urllib.request.Request(link)
    with urllib.request.urlopen(req) as res:
        print(dict(res.headers).get("X-Request-Id"))
