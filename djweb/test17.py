#!/usr/bin/env python3
# -*-coding:utf-8-*-
import urllib.request
import re
import os

url = r"file:///home/pc7/mlt/91.html"
title ="<title>(.*) .*"
# resolution = "<span id=\"resolution-val\" class=\"value .*\">\n                                    (.*)\n                                </span>"
resolution = "<span id=\"resolution-val\" class=\"value .*\".*>\n                                    (.*)\n                                </span>"
status = ";/span&gt;\">(.*)</span>            </span>"
Assignee = "</span></span>\n            (.*)\n        </span>"
bug = ["错误原因:<br>\n(.*)<br>", "错误原因:<br/>\n(.*)<br/>"]
print(urllib.request.urlopen(url).read().decode("utf-8"))
def web(reurl):
    web_source = urllib.request.urlopen(url).read().decode("utf-8")
    return re.compile(reurl).findall(web_source)


title_value = web(title)
title_strip = "".join(title_value)
title_join = title_strip.split(" ")

bug_value = web(bug[0])


if len(bug_value) == 0:
    bug_value = web(bug[1])

Bug_value = re.sub(r'Occurred', "", ''.join(bug_value), re.I)
print(Bug_value)

ID = title_join[0].strip("[]")
print(ID)
Title_value = ''.join(title_join[1:])
TiTle_value = re.sub(r'-', '',Title_value).replace(' ','')
print(TiTle_value)


status_value = web(status)[0]
print(status_value)
resolution_value = web(resolution)
print(resolution_value)
Assignee_value = web(Assignee)[0].replace(' ','')
print(Assignee_value)


liz = ["938", "648"]

terrace = re.compile(liz[0]).findall(TiTle_value)
if len(terrace) == 0:
    terrace = re.compile(liz[1]).findall(TiTle_value)



