#!/bin/bash
# sends json post request and display body
curl -s -X POST -H "Content-Type: application/json" -F "file=$2" "$1"
