#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import os
import datetime
# startTime=''
# startDateTime = time.strftime("%Y-%m-%d %H:%M:%S")
#
# endDateTime = time.strftime("%Y-%m-%d %H:%M:%S")
# print(startDateTime)
#
# phoneExeTime = (endDateTime - startDateTime)
# print(phoneExeTime)





# folder = "/home/pc7/pydjango/mtbf/djweb/htmlFolder"
phoneInfo = open("/home/pc7/pydjango/mtbf/djweb/htmlFolder/648TV/phoneInfo.txt", "r")
lines = phoneInfo.readlines()
def getBuildInfo():
    phoneVer = ""
    phoneIMEI = ""
    phoneDate = ""
    startTime = ""
    endTime = ""
    phoneExeTime = 0
    for line in lines:

        if line.find("buildModel==") != -1:  # get build version
            index = len("buildModel==")
            phoneModel = line[index:].rstrip()
        elif line.find("buildVersion==") != -1:  # get build date
            index = len("buildVersion==")
            phoneVer = line[index:].rstrip()
        elif line.find("buildDate==") != -1:  # get build date
            index = len("buildDate==")
            phoneDate = line[index:].rstrip()
        elif line.find("testStartTime==") != -1:  # get start time
            index = len("testStartTime==")
            startTime = line[index:].rstrip()
        elif line.find("testEndTime==") != -1:  # get end time
            index = len("testEndTime==")
            endTime = line[index:].rstrip()

    # startDateTime = datetime.strptime(startTime, "%Y-%m-%d %H:%M:%S")
    # endDateTime = datetime.strptime(endTime, "%Y-%m-%d %H:%M:%S")
    # phoneExeTime = (endDateTime - startDateTime).total_seconds() / 3600
    # phoneExeTime = round(phoneExeTime, 1)
    return phoneModel,phoneVer , phoneDate, startTime , endTime , phoneExeTime

phoneModel,phoneVer , phoneDate, startTime , endTime,phoneExeTime= getBuildInfo()


