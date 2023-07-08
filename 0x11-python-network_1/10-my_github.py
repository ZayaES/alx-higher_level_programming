#!/usr/bin/python3
"""connects with github api to collect id of user"""
import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    url = "https://api.github.com/users/{}".format(username)
    values = {"Authorization":
              "Bearer {}".format(password),
              "Accept": "application/vnd.github+json"}

    r = requests.get(url, headers=values)
    print(r.json().get("id"))
