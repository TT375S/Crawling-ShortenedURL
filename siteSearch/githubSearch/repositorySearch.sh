#!/bin/bash
curl -H "Authentication: token TOKEN" \
-H "Accept: application/vnd.github.mercy-preview+json" \
https://api.github.com/search/repositories?q=topic:ruby+topic:rails
