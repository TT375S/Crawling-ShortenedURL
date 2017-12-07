# -*- coding: utf-8 -*-
import datetime
import traceback
import urllib.parse
#import urllib.request
import urllib.error
import re
import sys
import time
import itertools
import string
import os


import domainSpecific
import subprocess

def res_cmd_lfeed(cmd):
  return subprocess.Popen(
      cmd, stdout=subprocess.PIPE,
      shell=True).stdout.readlines()

def res_cmd_no_lfeed(cmd):
  return [str(x).rstrip("\n") for x in res_cmd_lfeed(cmd)]



class BruteforceDriver:
    def __init__(self, agent):
        self.domainAgent = agent
        self.challengeChar = []
        for i in range(0,10):
            self.challengeChar.append(str(i))
        for i in string.ascii_lowercase[:26]:
            self.challengeChar.append(i)
        for i in string.ascii_uppercase[:26]:
            self.challengeChar.append(i)

        self.logFileData = datetime.datetime.now().strftime('%Y-%m-%d--%H-%M-%S')

        self.skip_to_textTuple = ()

    @staticmethod
    def writeLineOpenAndClose(fileName, mode, content):
            f = open(fileName, mode)
            f.write(content+"\n")
            f.close()

    def writeUrls(self, destUrl, shortUrl):
        if len(sys.argv) >= 3:
            self.writeLineOpenAndClose(sys.argv[2]+"-"+self.logFileData+".txt", "a", destUrl)
            if len(sys.argv) >= 4:
                self.writeLineOpenAndClose(sys.argv[3]+"-"+self.logFileData+".txt", "a", shortUrl)

    def main(self):
        #skip
        if len(sys.argv) >= 5:
            skip_to_text = sys.argv[4]
            for char in skip_to_text:
                self.skip_to_textTuple += (char,)
            print(self.skip_to_textTuple)


        for length in range(len("".join(self.skip_to_textTuple)), 20):
            #repeated permutation of [0-9a-zA-Z].
            challengeTexts = list(itertools.product(self.challengeChar, repeat=length) )
            
            prevRetriedChallengeText = challengeTexts[0]
            
            #skip researched pattern (specified by CLI argument)
            if length == len("".join(self.skip_to_textTuple)):
                skip_to_index = challengeTexts.index(self.skip_to_textTuple)
                del challengeTexts[0:skip_to_index]
                print("skip to: " + "".join(self.skip_to_textTuple) + " at index:" + str(skip_to_index), file = sys.stderr)
            
            timeoutCount = 0
            for challengeText in challengeTexts:
                print("".join(challengeText), file = sys.stderr)
                
                url = self.domainAgent.url + "".join(challengeText)

                try:
                    cmdResultLines = res_cmd_no_lfeed("curl --socks5-hostname localhost:9050 -I " + url)
                    
                    for line in cmdResultLines:
                        if "location" in line or "Location" in line:
                            destUrl = re.sub("(L|l)ocation: ", "", line)
                            print(destUrl)

                            print(url, file=sys.stderr)
                            
                            print("HIT: " + destUrl, file = sys.stderr)
                            print("".join(challengeText))
                            self.writeUrls(destUrl, url)
                            break

                #TODO: change 
                except KeyError:
                    timeoutCount += 1
                    
                    print("timeout: " + str(timeoutCount), file=sys.stderr)
                    print("caused by: "+ "".join(challengeText), file = sys.stderr)
                    
                    #log url cause timeout
                    f = open("timeOutURL" + self.logFileData + ".txt", "a")
                    f.write(url+"\n")
                    f.close()
                    
                    #Retry
                    if not challengeText == prevRetriedChallengeText:
                        #try again
                        challengeTexts.insert(0, challengeText)
                        prevRetriedChallengeText = challengeText
                    else:
                        print("Failed retring", file = sys.stderr)
                    continue
                except urllib.error.HTTPError:
                    print("httpError")
                    print (traceback.format_exc())
                    
                    #self.writeLineOpenAndClose("404URL-" + self.logFileData + ".txt", "a", url)
                    #self.writeUrls("404", url)
                    #
                    #continue
                except KeyboardInterrupt:
                    exit()
                except :
                    print(traceback.format_exc())
                    f = open("exceptionURL" + self.logFileData + ".txt", "a")
                    f.write(url+"\n")
                    f.close()
                    continue
        self.driver.quit()

if __name__ == '__main__':
    if len(sys.argv) <= 1: 
        print("Specify domain!")
        exit()

    domainAgent_class = getattr(domainSpecific, sys.argv[1])
    domainAgent = domainAgent_class()

    mainDriver = BruteforceDriver(domainAgent)
    mainDriver.main()
