#!/usr/bin/python3
"""
Python script that takes in a URL,sends a request to the URL and displays the
value of the X-Request-Id variablefound in the header of the response.
"""

if __name__ == '__main__':
    import sys
    import urllib.request
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        url_res = response.info()
        print(url_res['X-Request-Id'])
