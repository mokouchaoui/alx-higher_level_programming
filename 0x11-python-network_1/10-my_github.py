#!/usr/bin/python3
"""
Write a Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id
"""

if __name__ == "__main__":
    import sys
    import requests

    url = "https://api.github.com/user"
    response = requests.get(
        url, auth=requests.auth.HTTPBasicAuth(sys.argv[1], sys.argv[2])
    )
    res_dict = response.json()
    print(res_dict.get("id"))
