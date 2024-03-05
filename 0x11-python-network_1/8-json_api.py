#!/usr/bin/python3
"""
Write a Python script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import sys
import requests


if __name__ == "__main__":
    string = "" if len(sys.argv) == 1 else sys.argv[1]
    pay = {"q": string}

    req = requests.post("http://0.0.0.0:5000/search_user", data=pay)
    try:
        res = req.json()
        if res == {}:
            print("No result")
        else:
            print("[{}] {}".format(res.get("id"), res.get("name")))
    except ValueError:
        print("Not a valid JSON")
