#!/bin/bash
# cURL only methods
curl -sI "$@" | grep -i Allow: | awk -F": " '{print $2}'
