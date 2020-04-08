#!/bin/bash
# cURL a JSON file
curl -sH "Content-Type: application/json" --data @"$2" "$1"
