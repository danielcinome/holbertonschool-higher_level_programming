#!/bin/bash
# Only status code
curl -sLI "$@" -o /dev/null -w '%{http_code}' -s
