#!/usr/bin/python3
"""
Write a Python script that takes 2 arguments in order to solve this challenge.
The first argument will be the repository name
The second argument will be the owner name
You must use the packages requests and sys
You are not allowed to import packages other than requests and sys
You don’t need to check arguments passed to the script (number or type)
"""

if __name__ == "__main__":
    import sys
    import requests

    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])
    try:
        response = requests.get(url)
        res = response.json()
        for i in range(0, 10):
            print(
                "{}: {}".format(
                    res[i].get("sha"),
                    res[i].get("commit").get("author").get("name"),
                )
            )
    except Exception:
        pass
