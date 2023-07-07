#!/usr/bin/python3
"""prints error code when HTTP error occurs"""

import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    r = requests.get(url)
    if (r.status_code > 399):
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
