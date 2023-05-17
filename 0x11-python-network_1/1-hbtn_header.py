#!/usr/bin/python3
"""A script that displays the X-Request-Id header variable of a request to a given URL.

Usage: ./1-hbtn_header.py <URL>
"""
import sys
import urllib.request

url = sys.argv[1]

if __name__ == "__main__":

    with urllib.request.urlopen(url) as response:
        print(dict(response.headers).get("X-Request-Id"))
