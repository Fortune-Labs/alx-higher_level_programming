#!/usr/bin/python3
"""Python script that takes in a URL and an email, sends a POST request to a given URL with a given email.

Usage: ./2-post_email.py <URL> <email>
  - Displays the body of the response.
"""
import sys
import urllib.parse
import urllib.request

url = sys.argv[1]
email = sys.argv[2]

data = urllib.parse.urlencode({'email': email}).encode('utf-8')
req = urllib.request.Request(url, data=data, method='POST')

if __name__ == "__main__":
    with urllib.request.urlopen(req) as response:
      print(response.read().decode("utf-8"))
