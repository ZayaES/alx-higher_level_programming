#!/usr/bin/python3
"""displays the x-request-id in header of a requested url"""

import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        print(dict(response.headers).get("X-Request-Id"))
