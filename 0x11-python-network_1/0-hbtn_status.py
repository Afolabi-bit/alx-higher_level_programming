#!/usr/bin/python3
"""
   A python script that fetches
   https://alx-intranet.hbtn.io/status using urllib
"""
import urllib.request


if __name__ == "__main__":
    request = urllib.request.Request("https://alx-intranet.hbtn.io/status")
    with urllib.request.urlopen(request) as response:
        res = response.read()
        print("Body response:")
        print(f"\t- type: {type(res)}")
        print(f"\t- content: {res}")
        print("\t- utf8 content: {}".format(res.decode("utf-8")))
