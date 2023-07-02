#!/bin/bash
# sends json post request and display body
curl -s -X POST -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
