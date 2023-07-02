#!/bin/bash
# prints allowe verbs/methods only
curl -sI "$1" | grep Allow | cut -d " " -f 2-
