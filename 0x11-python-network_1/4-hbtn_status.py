#!/usr/bin/python3
""" fetches a url and displays response as formated"""

import requests


if __name__ == "__main__":
    r = requests.get("https://alx-intranet.hbtn.io/status")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))
