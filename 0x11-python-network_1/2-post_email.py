#!/usr/bin/python3
"""post email unto url"""

import sys
import urllib.request
import urllib.parse


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    values = {'email': email}
    data = urllib.parse.encode(values)
    data = values.encode('ascii')
    url = urllib.request.Request(url, data)
    with urllib.request.urlopen(url) as response:
        print(response.read())
    
