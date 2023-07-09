#!/usr/bin/python3
"""list all latests 10 commit of a repo"""
import requests
import sys


if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    url = "https://api.github.com/repos/{}/{})".format(
           owner_name, repo_name)
    params = {"per_page": 10}
    values = {"Authorization":
              "Bearer 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",
              "Accept": "application/vnd.github+json"}

    r = requests.get(url, headers=values, params=params)
    commits = r.json()
    try:
        for commit in commits:
            sha = commit["sha"]
            author_name = commit["sha"]["author"]["name"]
            print("{}: {}".format(sha, author_name))
    except Exception:
        pass
