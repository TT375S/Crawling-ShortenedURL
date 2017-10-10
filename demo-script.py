#!/usr/bin/env python
# -*- coding: utf-8 -*-

#It's a DEMO program.
#EXEC "example usage" in the README.

import subprocess
import sys

print("Input your Google Safe Brawsing API key:")
APIKey = input()

crawler = "./twitter-crawler/twitterCrawl-allDomain.py"
validator = "./linkValidator/linkValidator.py"
safetyChecker = "./linkSafetyChecker/linkSafetyChecker-google.py"

def makeCommand(filename, inputFile, outputFile):
    return "python3 " + filename +" < " +inputFile + " > "  + outputFile  


#collect short URL from twitter
subprocess.call(makeCommand(crawler, "serviceList-domain.txt", "shortURLfromTwitter.txt" ).strip().split(" ") )

#list short url's destinations.
subprocess.call(makeCommand(validator, "shortURLfromTwitter.txt", "linkDestination.txt" ).strip().split(" ") )

#check safety
subprocess.call(makeCommand(validator + " " + APIKey, "linkDestination.txt", "unsafeList.txt" ).strip().split(" ") )


