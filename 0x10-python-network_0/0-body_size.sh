#!/bin/bash
# connects to url and displays size of body
echo $(curl -s -o /dev/null -w "%{size_download}" "$1")
