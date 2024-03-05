#!/usr/bin/python3
"""
Task 4:
Fetches https://intranet.hbtn.io/status

4-hbtn_status.py
"""
import requests

if __name__ == "__main__":
    req = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(req.text)))
    print("\t- content: {}".format(req.text))
