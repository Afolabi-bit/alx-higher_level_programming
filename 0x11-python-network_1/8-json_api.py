#!/usr/bin/python3
"""
   Takes in a letter, sends a POST request to
   http://0.0.0.0:5000/search_user
   with the letter as a parameter
"""
import sys
import requests


if __name__ == "__main__":
    if len(sys.argv) == 1:
        letter = {"q": ""}
    else:
        letter = {"q": sys.argv[1]}

    res = requests.post("http://0.0.0.0:5000/search_user", data=letter)
    try:
        response = res.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
