import sys, json;

data = json.load(sys.stdin)

urlDic = {}

threatTypeDic = {}
platformTypeDic = {}

defaultThreatType = ["MALWARE", "SOCIAL_ENGINEERING", "UNWANTED_SOFTWARE", "POTENTIALLY_HARMFUL_APPLICATION", "THREAT_TYPE_UNSPECIFIED"]
defaultPlatformType = ["WINDOWS", "OSX","LINUX",  "ANDROID",  "IOS", "CHROME", "PLATFORM_TYPE_UNSPECIFIED"]
    
for threat in defaultThreatType:
    threatTypeDic.setdefault( threat, {})
    for platform in defaultPlatformType:
        threatTypeDic[threat].setdefault(platform, 0)

for platform in defaultPlatformType:
    platformTypeDic.setdefault( platform, {})
    for threat in defaultThreatType:
        platformTypeDic[platform].setdefault(threat, 0)

for result in data["matches"]:
    url = result["threat"]["url"]
    threatType = result["threatType"]
    platformType = result["platformType"]

    urlDic.setdefault(url, []) 
    urlDic[url].append( (threatType, platformType) )
    
    threatTypeDic[threatType][platformType] += 1

    platformTypeDic[platformType][threatType] += 1
#print(urlDic)

print("   ,", end='')
for platform in defaultPlatformType:
    print(platform +", ", end='')
print("")

for k, v in threatTypeDic.items():
    print(k +", ", end = '')
    for j, n in v.items():
        print(str(n) +", ", end = '')
    print("")

#for k, v in platformTypeDic.items():
#    print(k + ", " + str(v))

#print(threatTypeDic)
#print(platformTypeDic)
