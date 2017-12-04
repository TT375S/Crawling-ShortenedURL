#!/bin/bash
curl -H "Authentication: token TOKEN" \
-H "Accept: application/vnd.github.cloak-preview" \
https://api.github.com/search/commits?q=bit.ly
