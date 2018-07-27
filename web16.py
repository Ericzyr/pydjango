#!/usr/bin/env python
#_*_coding:utf-8_*_
# Author
import urllib
import urllib.request
import re
import os
import sys


url1 = sys.argv[1]
#url1=input("请输入文件路径：")
ulr = url1
requestcode = urllib.request.urlopen(ulr).read().decode("utf-8")

urlp = "<td>(.*)</td>"

urlre = "<td valign=\"top\" colspan=\"1\"><a href=\"(.*)\" target=\"_blank\">Click to open it</a></td>"

urlst =";\">\n\t	(.*)"

urlt = re.compile(urlre).findall(requestcode)

urltp = re.compile(urlp).findall(requestcode)

urltst = re.compile(urlst).findall(requestcode)


for i in urltst:
    platform = i[0:3]

pathcod1 = r"file://(.*)/.*.html$"

pathcode = re.compile(pathcod1).findall(ulr)


document = open("note.txt", "w", encoding="utf-8")
# print("一共发现了", len(urlt), "个Bug")
write_document = document.write("版本信息："+urltp[1]+"\r"+"一共发现了" + str(len(urlt)) + "个Bug""\r")
write_document = document.write("---------------------------------------------------------------"+"\r""\r")
for i in urlt:
    f = open(pathcode[0]+"/"+i, 'r')
    linenumber = f.readlines()[0:10]
    if "ANR" in linenumber[0]:
        wd = "(.*)/logstack.log"
        wordtile = re.findall(wd, i)[0]
        wordtilecode = "<td><a href=\""+wordtile+"\" target=\"_blank\">(.*)</a></td>"
        getword = re.compile(wordtilecode).findall(requestcode)
        # print("在"+getword[0]+"时发生了ANR")
        # print(pathcode[0]+"/"+i)
        write_document = document.write("【"+platform+"CIBN:"+urltp[1]+" STRESS"+"】"+"在"+getword[0]+"时发生了ANR""\r")
        write_document = document.write(pathcode[0]+"/"+i+"\r""\r")
        write_document = document.write(
            linenumber[0] + linenumber[1] + linenumber[2] + linenumber[3] + linenumber[4] + linenumber[5] + "\r")
        write_document = document.write("---------------------------------------------------------------" + "\r""\r")
    if "FATAL EXCEPTION" in linenumber[0]:
        wd = "(.*)/logstack.log"
        wordtile = re.findall(wd, i)[0]
        wordtilecode = "<td><a href=\"" + wordtile + "\" target=\"_blank\">(.*)</a></td>"
        getword = re.compile(wordtilecode).findall(requestcode)
        # print("在"+getword[0]+"时发生了FC")
        # print(pathcode[0]+"/"+i)
        write_document = document.write("【"+platform+"CIBN:"+urltp[1]+" STRESS"+"】"+"在"+getword[0]+"时发生了FC""\r")
        write_document = document.write(pathcode[0] + "/" + i + "\r""\r")
        write_document = document.write(
            linenumber[0] + linenumber[1] + linenumber[2] + linenumber[3] + linenumber[4] + linenumber[5] + "\r")
        write_document = document.write("---------------------------------------------------------------" + "\r""\r")
    if "pid:" in linenumber[3]:
        wd = "(.*)/logstack.log"
        wordtile = re.findall(wd, i)[0]
        # print(wordtile)
        wordtilecode = "<td><a href=\"" + wordtile + "\" target=\"_blank\">(.*)</a></td>"
        getword = re.compile(wordtilecode).findall(requestcode)
        # print("在"+getword[0]+"时发生了Tombstore")
        # print(pathcode[0]+"/"+i)
        write_document = document.write("【"+platform+"CIBN:"+urltp[1]+" STRESS"+"】"+"在" + getword[0] + "时发生了Tombstore""\r")
        write_document = document.write(pathcode[0] + "/" + i + "\r""\r")

    # print(linenumber[0], linenumber[1], linenumber[2],linenumber[3],linenumber[4],linenumber[5])
        write_document = document.write(
            linenumber[0] + linenumber[1] + linenumber[2]+linenumber[3]+linenumber[4]+linenumber[5]+"\r")
        write_document = document.write("---------------------------------------------------------------" + "\r""\r")
    f.close()
document.close()
os.system('xdg-open note.txt')
