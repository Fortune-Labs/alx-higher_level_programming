#!/usr/bin/python3
"""A python script that fetches https://intranet.hbtn.io/status."""
import urllib.request

url = 'https://alx-intranet.hbtn.io/status'

if __name__ == "__main__":
    with urllib.request.urlopen(url) as response:
        body = response.read().decode('utf-8')
        print("Body response:")
        print("\t- type: {}".format(type(r.text)))
        print("\t- content: {}".format(r.text))
