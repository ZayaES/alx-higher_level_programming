#!/usr/bin/python3
"""connects with github api to collect id of user"""
import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    url = "https://api.github.com/{}".format(username)
    values = {"Authourization": \
            "Bearer {}".format(password),\
            "X-GitGub-Api-Version": "2022-11-28"}

    r = requests.get(url, headers=values)
    print(r.json().get("id"))
