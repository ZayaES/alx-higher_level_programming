#!/bin/bash
# status code only
curl -sI -o /dev/null -w %{http_code} "$1"
