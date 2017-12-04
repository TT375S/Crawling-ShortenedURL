import sys
import json
import re
inputFileName = "repository.txt"

if len(sys.argv) >=2:
    inputFileName = sys.argv[1]

f = open(inputFileName)
jsonData = json.load(f)
f.close()

items = jsonData["items"]

for item in items:
    commit = item["commit"]
    commitMessage = commit["message"]
    urls = re.findall('(?:https?:\/\/|)[^\s ]+\/[0-9a-zA-Z]*' , commitMessage)
    for url in urls:
        print(url)
