#!/usr/bin/python3
""" requests a json file with inut letter"""

import sys
import requests

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"

    if len(sys.argv) < 2:
        let = ""
    else:
        let = sys.argv[1]
    value = {"q": let}

    r = requests.post(url, data=value)
    try:
        res = r.json()
        if res == {}:
            print("No result")
        else:
            print("[{}] {}".format(res.get("id"), res.get("name")))
    except ValueError:
        print("Not a valid JSON")
