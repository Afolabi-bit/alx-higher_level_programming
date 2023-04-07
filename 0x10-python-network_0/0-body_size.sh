#!/bin/bash
# This script takes a URL, sends a request to it and displays the size of itd response
curl -sI "$1" | wc -c
