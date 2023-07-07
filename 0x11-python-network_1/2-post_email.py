#!/usr/bin/python3
"""post email unto url"""

import sys
import urllib.request
import urllib.parse


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    values = {'email': email}
    data = urllib.parse.urlencode(values)
    data = data.encode("ascii")

    url = urllib.request.Request(url, data)
    with urllib.request.urlopen(url) as response:
        print(response.read().decode("utf-8"))
