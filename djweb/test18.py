#!/usr/bin/env python
#_*_coding:utf-8_*_
import plotly.plotly as py
import plotly.graph_objs as go
import os
import urllib.request
import re
paht_old = "/home/pc7/old_buglist/"

list_bug_old = os.listdir(paht_old)
listad_old = []
paht_old = "/home/pc7/old_buglist/"

list_bug_old = os.listdir(paht_old)
listad_old = []
for i in range(len(list_bug_old)):
    url_old = r"file://" + paht_old + list_bug_old[i]
    title_old = "<title>(.*) .*"
    resolution_old = "<span id=\"resolution-val\" class=\"value .*\".*>\n                                    (.*)\n                                </span>"
    status_old = ";/span&gt;\">(.*)</span>            </span>"
    Assignee_old = "</span></span>\n            (.*)\n        </span>"
    bug_old = ["错误原因:<br>\n(.*)<br>" , "错误原因:<br/>\n(.*)<br/>"]


    def web(reurl_old):
        web_source_old = urllib.request.urlopen(url_old).read().decode("utf-8")
        return re.compile(reurl_old).findall(web_source_old)


    title_value_old = web(title_old)
    title_strip_old = "".join(title_value_old)
    title_join_old = title_strip_old.split(" ")
    bug_value_old = web(bug_old[0])
    if len(bug_value_old) == 0:
        bug_value_old = web(bug_old[1])
    Error_Type_value_old = re.sub(r'Occurred' , "" , ''.join(bug_value_old) , re.I)
    ID_value_old = title_join_old[0].strip("[]")
    Titlee_value_old = ''.join(title_join_old[1:])
    Title_value_old = re.sub(r'-' , '' , Titlee_value_old).replace(' ' , '')
    status_value_old = web(status_old)[0]
    resolution_value_old = web(resolution_old)[0]
    Assignee_value_old = web(Assignee_old)[0].replace(' ' , '')
    lis_old = [Error_Type_value_old , ID_value_old , Title_value_old , status_value_old , Assignee_value_old ,
               resolution_value_old]
    listad_old.append(lis_old)

print(listad_old)