# -*- coding: utf-8 -*-
import datetime
import traceback
import urllib.parse
import urllib.request
import urllib.error
import re
import sys
import time
import itertools
import string
import os


import domainSpecific

#-Prepare tor (from https://stackoverflow.com/questions/711351/how-to-route-urllib-requests-through-the-tor-network)----
import socks
import socket

# This function has no DNS resolve
# it need to use the real ip adress to connect instead of www.google.com
def create_connection_fixed_dns_leak(address, timeout=None, source_address=None):
    sock = socks.socksocket()
    sock.connect(address)
    return sock

# MUST BE SET BEFORE IMPORTING URLLIB
socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9050)
# patch the socket module
socket.socket = socks.socksocket
socket.create_connection = create_connection_fixed_dns_leak

from urllib import request
#----

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
                    req = request.Request(url)
                    res = request.urlopen(req)

                    destUrl = res.geturl()
                    print(destUrl)

                    print(url, file=sys.stderr)
                    html = str(res.read())
                    
                    #The short url is valid!
                    if self.domainAgent.isValid(url, destUrl, html):
                        print("HIT: " + destUrl, file = sys.stderr)
                        print("".join(challengeText))
                        self.writeUrls(destUrl, url)
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
                    self.writeLineOpenAndClose("404URL-" + self.logFileData + ".txt", "a", url)
                    self.writeUrls(res.geturl(), url)
                    
                    continue
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
