# -*- coding: utf-8 -*-
import datetime
import traceback
import re
import sys
import time
import itertools
import string
import os




challengeChar = []
for i in range(0,10):
    challengeChar.append(str(i))
for i in string.ascii_lowercase[:26]:
    challengeChar.append(i)
for i in string.ascii_uppercase[:26]:
    challengeChar.append(i)



def writeLineOpenAndClose(fileName, mode, content):
        f = open(fileName, mode)
        f.write(content+"\n")
        f.close()

for length in range(1,6):
    output = open("cpat"+str(length)+".txt", "w")
    challengeTexts = list(itertools.product(challengeChar, repeat=length) )
    for text in challengeTexts:
        output.write("".join(text) + "\n")
    output.close()
