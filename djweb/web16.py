#!/usr/bin/env python
#_*_coding:utf-8_*_
# Author
import urllib
import urllib.request
import re
import os
import sys


# url1 = sys.argv[1]
#url1=input("请输入文件路径：")
ulr = r"file:///home/pc7/pydjango/djweb/apptest_tv/661.html"

requestcode = urllib.request.urlopen(ulr).read().decode("utf-8")
# print(requestcode)

urlp = "<td>(.*)</td>"

urlre = "<td valign=\"top\" colspan=\"1\"><a href=\"(.*)\" target=\"_blank\">Click to open it</a></td>"

urlst = ";\">\n\t	(.*)"


def getult(argsult):
    return re.compile(argsult).findall(requestcode)



urlt = getult(urlre)

urltp = getult(urlp)

urltst = getult(urlst)



strultp = ";".join(urltp)
# print(strultp)

swurl = "SW;(.*);Release Time"

SeleaseTimeurl = 'Release Time;(.*);Test Start Time'

TestTimeurl = 'Test Start Time;(.*);Test Stop Time'

TestStopurl = 'Test Stop Time;(.*);Test Total Execution Time'

SasePassRateurl = 'Case Pass Rate;(.*);<span class="passCount">STRESS Value</span>;'


def gets(args):
    get1 = re.compile(args).findall(strultp)
    get2 = ''.join(get1)
    return get2.split(";")


print(urltst)

SW = gets(swurl)[0]
print(SW)

SeleaseTime = gets(SeleaseTimeurl)
print(SeleaseTime)

TestTime = gets(TestTimeurl)[0][0:10]
print(TestTime)

TestStop = gets(TestStopurl)[0][0:10]
print(TestStop)

SasePassRate = gets(SasePassRateurl)
print(SasePassRate)

li = []
passvalue_list = []
Assigned_list = []
PassRate_list = []
Fail_list = []
FailRate_list = []
for i in range(len(urltst)):
    t = SasePassRate[i].strip('<span class=\"passCount\"/>')
    li.append(t)
    passvalue = t.split("/")

    Passvalue = passvalue[0]
    passvalue_list.append(Passvalue)
    print(Passvalue)

    passrode = passvalue[1].split('=')
    print(passrode)

    Assigned = passrode[0]
    Assigned_list.append(Assigned)
    print(Assigned)
    PassRate = passrode[1]
    PassRate_list.append(PassRate)
    print(PassRate)
    Fail = int(Assigned) - int(Passvalue)
    Fail_list.append(Fail)

    t = '%.2f' %(Fail / int(Assigned)*100)
    print(t)

    FailRate = str((Fail / int(Assigned)) * 100) + "%"
    print(str(FailRate) + "%")
    FailRate_list.append(FailRate)
    print("=================================================")
print(urltst)
print(li)
print(passvalue_list)
print(Assigned_list)
print(PassRate_list)
print(Fail_list)
print(FailRate_list)




# print(urltst)
# for i in urltst:
#     platform = i[0:3]
#
# pathcod1 = r"file://(.*)/.*.html$"
#
# pathcode = re.compile(pathcod1).findall(ulr)


# document = open("note.txt", "w", encoding="utf-8")
# # print("一共发现了", len(urlt), "个Bug")
# write_document = document.write("版本信息："+urltp[1]+"\r"+"一共发现了" + str(len(urlt)) + "个Bug""\r")
# write_document = document.write("---------------------------------------------------------------"+"\r""\r")
# for i in urlt:
#     f = open(pathcode[0]+"/"+i, 'r')
#     linenumber = f.readlines()[0:10]
#     if "ANR" in linenumber[0]:
#         wd = "(.*)/logstack.log"
#         wordtile = re.findall(wd, i)[0]
#         wordtilecode = "<td><a href=\""+wordtile+"\" target=\"_blank\">(.*)</a></td>"
#         getword = re.compile(wordtilecode).findall(requestcode)
#         # print("在"+getword[0]+"时发生了ANR")
#         # print(pathcode[0]+"/"+i)
#         write_document = document.write("【"+platform+"CIBN:"+urltp[1]+" STRESS"+"】"+"在"+getword[0]+"时发生了ANR""\r")
#         write_document = document.write(pathcode[0]+"/"+i+"\r""\r")
#         write_document = document.write(
#             linenumber[0] + linenumber[1] + linenumber[2] + linenumber[3] + linenumber[4] + linenumber[5] + "\r")
#         write_document = document.write("---------------------------------------------------------------" + "\r""\r")
#     if "FATAL EXCEPTION" in linenumber[0]:
#         wd = "(.*)/logstack.log"
#         wordtile = re.findall(wd, i)[0]
#         wordtilecode = "<td><a href=\"" + wordtile + "\" target=\"_blank\">(.*)</a></td>"
#         getword = re.compile(wordtilecode).findall(requestcode)
#         # print("在"+getword[0]+"时发生了FC")
#         # print(pathcode[0]+"/"+i)
#         write_document = document.write("【"+platform+"CIBN:"+urltp[1]+" STRESS"+"】"+"在"+getword[0]+"时发生了FC""\r")
#         write_document = document.write(pathcode[0] + "/" + i + "\r""\r")
#         write_document = document.write(
#             linenumber[0] + linenumber[1] + linenumber[2] + linenumber[3] + linenumber[4] + linenumber[5] + "\r")
#         write_document = document.write("---------------------------------------------------------------" + "\r""\r")
#     if "pid:" in linenumber[3]:
#         wd = "(.*)/logstack.log"
#         wordtile = re.findall(wd, i)[0]
#         # print(wordtile)
#         wordtilecode = "<td><a href=\"" + wordtile + "\" target=\"_blank\">(.*)</a></td>"
#         getword = re.compile(wordtilecode).findall(requestcode)
#         # print("在"+getword[0]+"时发生了Tombstore")
#         # print(pathcode[0]+"/"+i)
#         write_document = document.write("【"+platform+"CIBN:"+urltp[1]+" STRESS"+"】"+"在" + getword[0] + "时发生了Tombstore""\r")
#         write_document = document.write(pathcode[0] + "/" + i + "\r""\r")
#
#     # print(linenumber[0], linenumber[1], linenumber[2],linenumber[3],linenumber[4],linenumber[5])
#         write_document = document.write(
#             linenumber[0] + linenumber[1] + linenumber[2]+linenumber[3]+linenumber[4]+linenumber[5]+"\r")
#         write_document = document.write("---------------------------------------------------------------" + "\r""\r")
#     f.close()
# document.close()
# os.system('xdg-open note.txt')

ulr1 = r"file:///home/pc7/%E6%A1%8C%E9%9D%A2/12.html"

requestcode1 = urllib.request.urlopen(ulr1).read().decode("utf-8")
print(requestcode1)
re.compile(argsult).findall(requestcode)
