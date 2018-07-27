#!/usr/bin/env python
#_*_coding:utf-8_*_
# Author
import urllib
import urllib.request
import re
import os
import sys


ulr = r"file:///home/pc7/pydjango/djweb/apptest_TV/2018611_1125.html"

requestcode = urllib.request.urlopen(ulr).read().decode("utf-8")
# print(requestcode)

urlre = "<td valign=\"top\" colspan=\"1\"><a href=\"(.*)\" target=\"_blank\">Click to open it</a></td>"

urlt = re.compile(urlre).findall(requestcode)
print(urlt)


pathcod1 = r"file://(.*)/.*.html$"

pathcode = re.compile(pathcod1).findall(ulr)

print(pathcode)


print("一共发现了", len(urlt), "个Bug")
for i in urlt:
    f = open(pathcode[0]+"/"+i, 'r')
    linenumber = f.readlines()[0:3]
    if "ANR" in linenumber[0]:
        wd = "(.*)/logstack.log"
        wordtile = re.findall(wd, i)[0]
        wordtilecode = "<td><a href=\""+wordtile+"\" target=\"_blank\">(.*)</a></td>"
        getword = re.compile(wordtilecode).findall(requestcode)
        print("在"+getword[0]+"时发生了ANR")
        print(pathcode[0]+"/"+i)
    if "FATAL EXCEPTION" in linenumber[0]:
        wd = "(.*)/logstack.log"
        wordtile = re.findall(wd, i)[0]
        wordtilecode = "<td><a href=\"" + wordtile + "\" target=\"_blank\">(.*)</a></td>"
        getword = re.compile(wordtilecode).findall(requestcode)
        print("在"+getword[0]+"时发生了FC")
        print(pathcode[0]+"/"+i)
    print(linenumber[0], linenumber[1], linenumber[2])
    f.close()
