#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
r = os.popen("pwd").read()
path1 = r.rsplit()[0]+"/htmlFolder"
# path = r.rsplit()[0]+"/htmlFolder/648TV/phoneInfo.txt"
# phoneInfo = open(path, "r")
# lines = phoneInfo.readlines()
# print(lines)

LOG_SUFFIX = "/case.log"
LOG_INFO = "/logstack.log"
FLAG_PASS = "OK (1 test)"

import re

def getFolderList(folder):
    pList = []
    for f in os.listdir(folder):
        if os.path.isdir(os.path.join(folder, f)):
            pList.append(os.path.join(folder, f))
    pList.sort(key=lambda x: os.stat(x).st_ctime)
    return pList


a=getFolderList(path1)


Loop = getFolderList(a[0])




print(Loop[0])
p=getFolderList(Loop[0])
print(p[0])


path = p[0]+"/case.log"

print(path)
logcase = open(path, "r")
lines = logcase.readlines()



class LogParser():
    def __init__(self , planned , folderlist):
        # 		print folderlist
        self.resultSheet = []
        # 		self.executed = len(folderlist)
        self.executed = 0
        self.summarySheet = {'pass': 0 , 'plan': planned , 'exed': self.executed , 'tb': 0 , 'anr': 0 , 'fc': 0 ,
                             'reset': 0}
        for folder in folderlist:
            self.resultSheet.append(self.parse_log(folder))

    def parse_log(self , folder):
        # current case properties
        resultdata = {}
        casechname = ""
        caseclass = ""
        casename = ""
        exetime = ""
        failreason = ""
        casestep = ""
        ispass = "fail"
        screencap = ""
        logtrack = ""
        anrCount = ""
        fcCount = ""
        tombstoneCount = ""
        resetCount = ""
        resultdata["anrCount"] = 0
        resultdata["tombstoneCount"] = 0
        resultdata["fcCount"] = 0
        resultdata["resetCount"] = 0
        isFC = False
        isTB = False
        isANR = False
        isRS = False
        stepindex = 0
        try:
            logfile = open(folder + LOG_SUFFIX , "r")
            lines = logfile.readlines()
        except IOError as e:
            lines = ""
            lines_logcat = ""
        # get case dir
        _path = folder.split(os.sep)[1:]
        resultdata["caseurl"] = os.path.join(*_path)
        # print resultdata["caseurl"]
        for line in lines:

            if line.find("INSTRUMENTATION_STATUS: title=") != -1:  # get case chinese name
                index = len("INSTRUMENTATION_STATUS: title=")
                casechname = line[index:].rstrip()
                resultdata["casechname"] = casechname
            elif line.find("INSTRUMENTATION_STATUS: class=") != -1:  # get case class
                index = len("INSTRUMENTATION_STATUS: class=")
                caseclass = line[index:].rstrip()
                resultdata["caseclass"] = caseclass
            elif line.find("INSTRUMENTATION_STATUS: test=") != -1:  # get case name
                index = len("INSTRUMENTATION_STATUS: test=")
                casename = line[index:].rstrip()
                resultdata["casename"] = casename
            elif line.find("Time: ") != -1:  # record execute time
                self.summarySheet['exed'] += 1
                #				self.executed += 1
                index = len("Time: ")
                exetime = line[index:].rstrip()
                resultdata["exetime"] = exetime
            elif line.find("INSTRUMENTATION_STATUS: caseStep=") != -1:  # get case step
                stepindex += 1
                line = re.sub(r'INSTRUMENTATION_STATUS: caseStep=\d?\d?\.?' , str(stepindex) + '.' , line , 1).rstrip()
                casestep += line + "\n"
            elif line.find("INSTRUMENTATION_STATUS: screenshot=") != -1:  # get screenshot info
                index = len("INSTRUMENTATION_STATUS: screenshot=")
                screencap = line[index:].rstrip()
                resultdata["screencap"] = screencap
            elif line.find("INSTRUMENTATION_STATUS: logstack=") != -1:  # get logstack info
                index = len("INSTRUMENTATION_STATUS: logstack=")
                logstack = line[index:].rstrip()
                resultdata["logstack"] = logstack
            elif line.find("INSTRUMENTATION_STATUS: stack=") != -1:  # record fail reason
                index = len("INSTRUMENTATION_STATUS: stack=")
                failreason = line[index:].rstrip()
                if failreason.find("ANR occurred") != -1:
                    if isANR == False:
                        isANR = True
                        resultdata["anrCount"] += 1
                        ispass = "ANR"
                elif failreason.find("FC occurred") != -1:
                    if isFC == False:
                        isFC = True
                        resultdata["fcCount"] += 1
                        ispass = "FC"
                resultdata["failreason"] = "错误原因:\n" + failreason
            elif line.find("INSTRUMENTATION_STATUS: TOMBSTONES=") != -1:  # get tombstone
                if isTB == False:
                    isTB = True
                    resultdata["tombstoneCount"] += 1
                    ispass = "Tombstone"
                resultdata["failreason"] = "错误原因:\n"
            elif line.find("INSTRUMENTATION_STATUS: ANR=") != -1:  # get anr
                if isANR == False:
                    isANR = True
                    resultdata["anrCount"] += 1
                    ispass = "ANR"
                resultdata["failreason"] = "错误原因:\n"
            elif line.find("ANR occurred") != -1:  # get anr
                if isANR == False:
                    isANR = True
                    resultdata["anrCount"] += 1
                    ispass = "ANR"
                resultdata["failreason"] = "错误原因:\n"
            elif line.find("FC occurred") != -1:  # get fc
                if isFC == False:
                    isFC = True
                    resultdata["fcCount"] += 1
                    ispass = "FC"
                resultdata["failreason"] = "错误原因:\n"
            elif line.find("Tombstone occurred") != -1:  # get tombstone
                if isTB == False:
                    isTB = True
                    resultdata["tombstoneCount"] += 1
                    ispass = "Tombstone"
                resultdata["failreason"] = "错误原因:\n"
            elif line.find("Reboot occurred") != -1:  # get reboot
                if isRS == False:
                    isRS = True
                    resultdata["resetCount"] += 1
                    ispass = "Reset"
                resultdata["failreason"] = "错误原因:\n"
            elif line.find(FLAG_PASS) != -1:  # record pass or fail
                ispass = "pass"
        resultdata["ispass"] = ispass
        resultdata["casestep"] = casestep
        if (len(exetime) == 0):
            if ispass == "fail":
                ispass = "notrun"
                resultdata["ispass"] = ispass
        if ispass == 'pass':
            self.summarySheet['pass'] += 1
        if isFC:
            self.summarySheet['fc'] += resultdata["fcCount"]
        if isTB:
            resultdata["failreason"] += "\n Tombstone Occurred"
            self.summarySheet['tb'] += resultdata["tombstoneCount"]
        if isANR:
            resultdata["failreason"] += "\n ANR Occurred"
            self.summarySheet['anr'] += resultdata["anrCount"]
        if isRS:
            resultdata["failreason"] += "\n Reboot Occurred"
            self.summarySheet['reset'] += resultdata["resetCount"]
        if (caseclass == "" and casename == ""):
            resultdata["casename"] = folder
            resultdata["casechname"] = "case.log不存在"
        return resultdata

    def getResultData(self):
        return self.resultSheet

    def getSummaryData(self):
        self.summarySheet['exed'] = self.executed
        self.summarySheet['fail'] = self.executed - self.summarySheet['pass']
        self.summarySheet['notrun'] = int(self.summarySheet['plan']) - self.executed
        return self.summarySheet

def getLoopData(logFolder):
    caseLogList = []
    for folder in os.listdir(logFolder):
        if os.path.isdir(os.path.join(logFolder , folder)):
            caseLogList.append(os.path.join(logFolder , folder))
    caseLogList.sort(key=lambda x: os.stat(x).st_ctime)
    _p = LogParser(4, caseLogList)
    return _p



t = getLoopData("/home/pc7/pydjango/mtbf/djweb/htmlFolder/648TV/LOOP1/testDesktop_20180509_153433")
z=t.parse_log("/home/pc7/pydjango/mtbf/djweb/htmlFolder/648TV/LOOP1/testDesktop_20180509_153433")
print(z)
print('ispass:', z['ispass'])
print("caseclass:", z['caseclass'])
print('casename:', z['casename'])
print('casestep:', z['casestep'])

print('fcCount:', z['fcCount'])
print('tombstoneCount', z['tombstoneCount'])
print('anrCount', z['anrCount'])
print('exetime', z['exetime'])
print('resetCount', z['resetCount'])
print("Acaseurl",z['caseurl'])





    #
    # dict1 = {'Name': 'Runoob' , 'Age': 7 , 'Class': 'First'}
    #
    # # 字典的访问
    # print('Name:' , dict1['Name'])
    # print('Age:' , dict1['Age'])
#
# def getBuildInfo():
#     for line in lines:
#         if line.find("title=") != -1:  # get build version
#             index = len("INSTRUMENTATION_STATUS: title=")
#             phonetitle = line[index:].rstrip()
#         elif line.find("INSTRUMENTATION_STATUS: caseStep=") != -1:  # get build date
#             index = len("INSTRUMENTATION_STATUS: caseStep=")
#             caseStep = line[index:].rstrip()
#             print(caseStep)
#         elif line.find("Time:") != -1:  # get build date
#             index = len("Time:")
#             runtime = line[index:].rstrip()
#         elif line.find("INSTRUMENTATION_STATUS: class=") != -1:  # get start time
#             index = len("INSTRUMENTATION_STATUS: class=")
#             top = line[index:].rstrip()
#         elif line.find("testEndTime==") != -1:  # get end time
#             index = len("testEndTime==")
#             endTime = line[index:].rstrip()
#     return phonetitle, caseStep,runtime,top
#
#
# phonetitle, caseStep, runtime,top = getBuildInfo()
#
# print(phonetitle)
# print(caseStep)
# print(runtime)
# print(top)