#!/bin/bash
# curl
curl -sI "$1" | sed -n 's/Allow: //p'
