#!/usr/bin/env python3
# -*-coding:utf-8-*-
import os

# localpahth = os.popen("pwd").read()
# rootFolder = str(localpahth.rsplit()[0]) + "/apptest_TV"
# rootFolder1 = "/home/pc7/pydjango/djweb4/logcat/apptest_TV"
# print(rootFolder)
# print(rootFolder1)
#
# localpahth1 = os.popen("pwd").read()
# rootFolder1 = str(localpahth1.rsplit()[0]) + "/apptest_TV"
# rootFolder2 = rootFolder1
# print(rootFolder2)
#

t = ['648TV', 'LOOP1', 'testDesktop_20180509_153433']
z = os.path.join(t)
resultdata={}
resultdata["caseurl"] = os.path.join(*t)
print(resultdata["caseurl"])