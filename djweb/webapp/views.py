from django.http import HttpResponse , FileResponse
from django.shortcuts import render
from webapp import models
from django.conf import settings
import urllib.request
import re
import urllib.request
import os
import shutil

def index(request):
    if request.method == 'POST':
        user_name = request.POST.get('username', None)
        pass_word = request.POST.get('password', None)
        models.wesheet.objects.create(user=user_name, pwd=pass_word)
        if user_name == 'root' and pass_word == 'pass':
            us = user_name
            pa = pass_word

    pw = os.path.dirname(os.getcwd())
    pwz = pw + '/djweb/templates/Mstar6A938/'

    listpw = os.listdir(pwz)


    pwx = pw + '/djweb/templates/Mstar6A648/'

    listpx = os.listdir(pwx)


    return render(request, 'index.html',locals())


def login(request):
    return render(request , 'login.html')


def Ms938reportupload(request):
    pw = os.path.dirname(os.getcwd())
    pwz = pw + '/djweb/media/938bugweb/newbug/'
    listpw = os.listdir(pwz)
    pwx = pw + '/djweb/media/938bugweb/oldbug/'
    listpx = os.listdir(pwx)

    if request.method == 'POST':
        wefile = request.POST.get('name')
        wefil = request.POST.get('submit')

        newold = wefil.rsplit()[1]


        print(wefile)
        print(wefil)


        if newold == 'newbug':
            ptnew = os.getcwd()+'/media/938bugweb/newbug/'+wefile
            if os.path.exists(ptnew):
                os.remove(ptnew)
        elif newold == 'oldbug':
            ptold = os.getcwd() + '/media/938bugweb/oldbug/' + wefile
            if os.path.exists(ptold):
                os.remove(ptold)
    return render(request, 'Ms938reportupload.html', locals())

def Ms648reportupload(request):
    pw = os.path.dirname(os.getcwd())
    pwz = pw + '/djweb/media/648bugweb/newbug/'
    listpw = os.listdir(pwz)

    pwx = pw + '/djweb/media/648bugweb/oldbug/'
    listpx = os.listdir(pwx)

    if request.method == 'POST':
        wefile = request.POST.get('name')
        wefil = request.POST.get('submit')

        newold = wefil.rsplit()[1]
        if newold == 'newbug':
            ptnew = os.getcwd()+'/media/648bugweb/newbug/'+wefile
            if os.path.exists(ptnew):
                os.remove(ptnew)
        elif newold == 'oldbug':
            ptold = os.getcwd() + '/media/648bugweb/oldbug/' + wefile
            if os.path.exists(ptold):
                os.remove(ptold)


    return render(request, 'Ms648reportupload.html', locals())




def Ms938uploadnew(request):
    if request.method == 'POST':

        # 然后就是关键的读取上传的文件了，如图，导入settings。
        # 用FILES[‘testimg’]来获取文件，然后把media所在路径和文件名拼接在一起，然后用open创建新的文件，然后再把上传的文件内容写入到新创建的文件里面即可。Img.chunks()
        # 表示分割获取（防止文件太大）。

        img = request.FILES['newbug938']

        number = (str(img)[0])

        imgname = '%s/%s' % (settings.MEDIA_ROOT +'/938bugweb'+'/newbug', img.name)
        with open(imgname, 'wb')as f:
            for fimg in img.chunks():
                f.write(fimg)
        return HttpResponse('ok')
    else:
        return HttpResponse('no')



def Ms938uploadold(request):
    if request.method == 'POST':

        # 然后就是关键的读取上传的文件了，如图，导入settings。
        # 用FILES[‘testimg’]来获取文件，然后把media所在路径和文件名拼接在一起，然后用open创建新的文件，然后再把上传的文件内容写入到新创建的文件里面即可。Img.chunks()
        # 表示分割获取（防止文件太大）。

        img = request.FILES['oldbug938']
        print(img)
        number = (str(img)[0])
        print(number)
        imgname = '%s/%s' % (settings.MEDIA_ROOT +'/938bugweb'+'/oldbug', img.name)
        with open(imgname, 'wb')as f:
            for fimg in img.chunks():
                f.write(fimg)
        return HttpResponse('ok')
    else:
        return HttpResponse('no')







def Ms648uploadnew(request):
    if request.method == 'POST':
        img = request.FILES['newbug648']
        print(img)
        number = (str(img)[0])
        print(number)
        imgname = '%s/%s' % (settings.MEDIA_ROOT +'/648bugweb'+'/newbug', img.name)
        print(imgname)
        with open(imgname, 'wb')as f:
            for fimg in img.chunks():
                f.write(fimg)
        return HttpResponse('ok')
    else:
        return HttpResponse('no')

def Ms648uploadold(request):
    if request.method == 'POST':
        img = request.FILES['oldbug648']
        imgname = '%s/%s' % (settings.MEDIA_ROOT +'/648bugweb'+'/oldbug', img.name)
        with open(imgname, 'wb')as f:
            for fimg in img.chunks():
                f.write(fimg)
        return HttpResponse('ok')
    else:
        return HttpResponse('no')


def ms938report(request):


    # pahtt = "/home/pc7/mlt/"
    # list_bug = os.listdir(pahtt)[0]

    ulr = r"file:///home/pc7/pydjango/djweb/media/938bugweb/LeTV STRESS Report.html"

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


    swurl = "SW;(.*);Release Time"

    SeleaseTimeurl = 'Release Time;(.*);Test Start Time'

    TestTimeurl = 'Test Start Time;(.*);Test Stop Time'

    TestStopurl = 'Test Stop Time;(.*);Test Total Execution Time'

    SasePassRateurl = 'Case Pass Rate;(.*);<span class="passCount">STRESS Value</span>;'

    def gets(args):
        get1 = re.compile(args).findall(strultp)
        get2 = ''.join(get1)
        return get2.split(";")

    SW = gets(swurl)[0]
    # print(SW)

    SeleaseTime = gets(SeleaseTimeurl)
    # print(SeleaseTime)

    TestTime = gets(TestTimeurl)[0][0:10]
    # print(TestTime)

    TestStop = gets(TestStopurl)[0][0:10]
    # print(TestStop)

    SasePassRate = gets(SasePassRateurl)
    # print(SasePassRate)

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
        # print(Passvalue)

        passrode = passvalue[1].split('=')
        # print(passrode)

        Assigned = passrode[0]
        Assigned_list.append(Assigned)
        # print(Assigned)
        PassRate = passrode[1]
        PassRate_list.append(PassRate)
        # print(PassRate)
        Fail = int(Assigned) - int(Passvalue)
        Fail_list.append(Fail)
        FailRate = str("%.2f" % ((Fail / int(Assigned)) * 100)) + "%"
        # print(str(FailRate) + "%")
        FailRate_list.append(FailRate)

    for i in range(len(urltst)):
        urltst[i] = {'Features': urltst[i], 'Assigned': Assigned_list[i], 'passvalue': passvalue_list[i],
                     'PassRate': PassRate_list[i], 'Fail': Fail_list[i],'FailRate':FailRate_list[i]}


    # 这一部分是在报bug模块
    paht = "/home/pc7/pydjango/djweb/media/938bugweb/newbug/"

    list_bug = os.listdir(paht)
    listad = []
    for i in range(len(list_bug)):
        url = r"file://"+paht+list_bug[i]
        title = "<title>(.*) .*"
        resolution = "<span id=\"resolution-val\" class=\"value .*\".*>\n                                    (.*)\n                                </span>"
        status = ";/span&gt;\">(.*)</span>            </span>"
        Assignee = "</span></span>\n            (.*)\n        </span>"
        bug = ["错误原因:<br>\n(.*)<br>", "错误原因:<br/>\n(.*)<br/>"]
        bug_nub = "发生次数:<br/>\n(.*)<br/>"
        def web(reurl):
            web_source = urllib.request.urlopen(url).read().decode("utf-8")
            return re.compile(reurl).findall(web_source)
        title_value = web(title)
        title_strip = "".join(title_value)
        title_join = title_strip.split(" ")
        bug_value = web(bug[0])
        if len(bug_value) == 0:
            bug_value = web(bug[1])
        Error_Type_value = re.sub(r'Occurred', "", ''.join(bug_value), re.I)
        ID_value = title_join[0].strip("[]")
        Titlee_value = ''.join(title_join[1:])
        Title_value = re.sub(r'-', '', Titlee_value).replace(' ', '')

        liz = ["938", "648"]
        terrace = re.compile(liz[0]).findall(Titlee_value)
        if len(terrace) == 0:
            terrace = re.compile(liz[1]).findall(Titlee_value)
        Terrace = ''.join(terrace)
        status_value = web(status)[0]
        resolution_value = web(resolution)[0]

        Assignee_value = web(Assignee)[0].replace(' ', '')
        occurred_Times = web(bug_nub)
        occurred_times = "".join(occurred_Times)

        lis = [Error_Type_value,ID_value,Title_value,status_value,Assignee_value,resolution_value,occurred_times]
        listad.append(lis)
        opennumber = len(listad)
    for i in range(len(listad)):
        listad[i] = {'Error_Type_value': listad[i][0],'ID_value': listad[i][1], 'Title_value': listad[i][2],
                     'status_value': listad[i][3],'Assignee_value': listad[i][4],
                     'resolution_value': listad[i][5],"occurred_times":listad[i][6]}


    # 这一部分是在old报bug模块
    paht_old = "/home/pc7/pydjango/djweb/media/938bugweb/oldbug/"

    list_bug_old = os.listdir(paht_old)
    listad_old = []


    for i in range(len(list_bug_old)):
        url_old = r"file://" + paht_old + list_bug_old[i]
        title_old = "<title>(.*) .*"
        resolution_old = "<span id=\"resolution-val\" class=\"value .*\".*>\n                                    (.*)\n                                </span>"
        status_old = ";/span&gt;\">(.*)</span>            </span>"
        Assignee_old = "</span></span>\n            (.*)\n        </span>"
        bug_old = ["错误原因:<br>\n(.*)<br>" , "错误原因:<br/>\n(.*)<br/>"]
        bug_nub_old = "发生次数:<br/>\n(.*)<br/>"
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
        Title_value_old = re.sub(r'-' , '' , Titlee_value_old).replace(' ', '')
        status_value_old = web(status_old)[0]
        resolution_value_old = web(resolution_old)[0]
        Assignee_value_old = web(Assignee_old)[0].replace(' ' , '')
        occurred_Times_old = web(bug_nub_old)
        occurred_times_old = "".join(occurred_Times_old)

        lis_old = [Error_Type_value_old , ID_value_old , Title_value_old , status_value_old , Assignee_value_old , resolution_value_old,occurred_times_old]
        listad_old.append(lis_old)

    for i in range(len(listad_old)):
        listad_old[i] = {'Error_Type_value_old': listad_old[i][0] , 'ID_value_old': listad_old[i][1] , 'Title_value_old': listad_old[i][2],
                     'status_value_old': listad_old[i][3], 'Assignee_value_old': listad_old[i][4],
                         'resolution_value_old': listad_old[i][5],'occurred_times_old':listad_old[i][6]}

    openNumber = request.POST.get('openNumber')
    closeNumber = request.POST.get('closeNumber', None)
    urgency = request.POST.get('urgency', None)
    highNumber = request.POST.get('highNumber', None)
    ordinaryNumber = request.POST.get('ordinaryNumber', None)
    minorNumber = request.POST.get('minorNumber', None)
    noNumber = request.POST.get('noNumber', None)


    return render(request, 'ms938report.html', locals())

    # def getHtml(url):
    #     html = urllib.request.urlopen(url).read()
    #     return html
    #
    # def saveHtml(file_name , file_content):
    #     #    注意windows文件命名的禁用符，比如 /
    #     with open(file_name.replace('/' , '_') + ".html" , "wb") as f:
    #         #   写文件用bytes而不是str，所以要转码
    #         f.write(file_content)
    #
    # aurl = "http://127.0.0.1:8000/ms648report/"
    # html = getHtml(aurl)
    # saveHtml(123, html)






def ms648report(request):


    # pahtt = "/home/pc7/mlt/"
    # list_bug = os.listdir(pahtt)[0]

    ulr = r"file:///home/pc7/pydjango/djweb/media/648bugweb/LeTV STRESS Report.html"

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


    swurl = "SW;(.*);Release Time"

    SeleaseTimeurl = 'Release Time;(.*);Test Start Time'

    TestTimeurl = 'Test Start Time;(.*);Test Stop Time'

    TestStopurl = 'Test Stop Time;(.*);Test Total Execution Time'

    SasePassRateurl = 'Case Pass Rate;(.*);<span class="passCount">STRESS Value</span>;'

    def gets(args):
        get1 = re.compile(args).findall(strultp)
        get2 = ''.join(get1)
        return get2.split(";")

    SW = gets(swurl)[0]
    # print(SW)

    SeleaseTime = gets(SeleaseTimeurl)
    # print(SeleaseTime)

    TestTime = gets(TestTimeurl)[0][0:10]
    # print(TestTime)

    TestStop = gets(TestStopurl)[0][0:10]
    # print(TestStop)

    SasePassRate = gets(SasePassRateurl)
    # print(SasePassRate)

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
        # print(Passvalue)

        passrode = passvalue[1].split('=')
        # print(passrode)

        Assigned = passrode[0]
        Assigned_list.append(Assigned)
        # print(Assigned)
        PassRate = passrode[1]
        PassRate_list.append(PassRate)
        # print(PassRate)
        Fail = int(Assigned) - int(Passvalue)
        Fail_list.append(Fail)
        FailRate = str("%.2f" % ((Fail / int(Assigned)) * 100)) + "%"
        # print(str(FailRate) + "%")
        FailRate_list.append(FailRate)

    for i in range(len(urltst)):
        urltst[i] = {'Features': urltst[i], 'Assigned': Assigned_list[i], 'passvalue': passvalue_list[i],
                     'PassRate': PassRate_list[i], 'Fail': Fail_list[i],'FailRate':FailRate_list[i]}


    # 这一部分是在报bug模块
    paht = "/home/pc7/pydjango/djweb/media/648bugweb/newbug/"

    list_bug = os.listdir(paht)
    listad = []
    for i in range(len(list_bug)):
        url = r"file://"+paht+list_bug[i]
        title = "<title>(.*) .*"
        resolution = "<span id=\"resolution-val\" class=\"value .*\".*>\n                                    (.*)\n                                </span>"
        status = ";/span&gt;\">(.*)</span>            </span>"
        Assignee = "</span></span>\n            (.*)\n        </span>"
        bug = ["错误原因:<br>\n(.*)<br>", "错误原因:<br/>\n(.*)<br/>"]
        bug_nub = "发生次数:<br/>\n(.*)<br/>"
        def web(reurl):
            web_source = urllib.request.urlopen(url).read().decode("utf-8")
            return re.compile(reurl).findall(web_source)
        title_value = web(title)
        title_strip = "".join(title_value)
        title_join = title_strip.split(" ")
        bug_value = web(bug[0])
        if len(bug_value) == 0:
            bug_value = web(bug[1])
        Error_Type_value = re.sub(r'Occurred', "", ''.join(bug_value), re.I)
        ID_value = title_join[0].strip("[]")
        Titlee_value = ''.join(title_join[1:])
        Title_value = re.sub(r'-', '', Titlee_value).replace(' ', '')

        liz = ["938", "648"]
        terrace = re.compile(liz[0]).findall(Titlee_value)
        if len(terrace) == 0:
            terrace = re.compile(liz[1]).findall(Titlee_value)
        Terrace = ''.join(terrace)
        status_value = web(status)[0]
        resolution_value = web(resolution)[0]

        Assignee_value = web(Assignee)[0].replace(' ', '')
        occurred_Times = web(bug_nub)
        occurred_times = "".join(occurred_Times)

        lis = [Error_Type_value,ID_value,Title_value,status_value,Assignee_value,resolution_value,occurred_times]
        listad.append(lis)
        opennumber = len(listad)
    for i in range(len(listad)):
        listad[i] = {'Error_Type_value': listad[i][0],'ID_value': listad[i][1], 'Title_value': listad[i][2],
                     'status_value': listad[i][3],'Assignee_value': listad[i][4],
                     'resolution_value': listad[i][5],"occurred_times":listad[i][6]}


    # 这一部分是在old报bug模块
    paht_old = "/home/pc7/pydjango/djweb/media/648bugweb/oldbug/"

    list_bug_old = os.listdir(paht_old)
    listad_old = []


    for i in range(len(list_bug_old)):
        url_old = r"file://" + paht_old + list_bug_old[i]
        title_old = "<title>(.*) .*"
        resolution_old = "<span id=\"resolution-val\" class=\"value .*\".*>\n                                    (.*)\n                                </span>"
        status_old = ";/span&gt;\">(.*)</span>            </span>"
        Assignee_old = "</span></span>\n            (.*)\n        </span>"
        bug_old = ["错误原因:<br>\n(.*)<br>" , "错误原因:<br/>\n(.*)<br/>"]
        bug_nub_old = "发生次数:<br/>\n(.*)<br/>"
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
        Title_value_old = re.sub(r'-' , '' , Titlee_value_old).replace(' ', '')
        status_value_old = web(status_old)[0]
        resolution_value_old = web(resolution_old)[0]
        Assignee_value_old = web(Assignee_old)[0].replace(' ' , '')
        occurred_Times_old = web(bug_nub_old)
        occurred_times_old = "".join(occurred_Times_old)

        lis_old = [Error_Type_value_old , ID_value_old , Title_value_old , status_value_old , Assignee_value_old , resolution_value_old,occurred_times_old]
        listad_old.append(lis_old)

    for i in range(len(listad_old)):
        listad_old[i] = {'Error_Type_value_old': listad_old[i][0] , 'ID_value_old': listad_old[i][1] , 'Title_value_old': listad_old[i][2],
                     'status_value_old': listad_old[i][3], 'Assignee_value_old': listad_old[i][4],
                         'resolution_value_old': listad_old[i][5],'occurred_times_old':listad_old[i][6]}
    openNumber = request.POST.get('openNumber', None)
    closeNumber = request.POST.get('closeNumber', None)
    urgency = request.POST.get('urgency', None)
    highNumber = request.POST.get('highNumber', None)
    ordinaryNumber = request.POST.get('ordinaryNumber', None)
    minorNumber = request.POST.get('minorNumber', None)
    noNumber = request.POST.get('noNumber', None)

    return render(request, 'ms648report.html', locals())

def ms648reportok(request):


    # pahtt = "/home/pc7/mlt/"
    # list_bug = os.listdir(pahtt)[0]

    ulr = r"file:///home/pc7/pydjango/djweb/media/648bugweb/LeTV STRESS Report.html"

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


    swurl = "SW;(.*);Release Time"

    SeleaseTimeurl = 'Release Time;(.*);Test Start Time'

    TestTimeurl = 'Test Start Time;(.*);Test Stop Time'

    TestStopurl = 'Test Stop Time;(.*);Test Total Execution Time'

    SasePassRateurl = 'Case Pass Rate;(.*);<span class="passCount">STRESS Value</span>;'

    def gets(args):
        get1 = re.compile(args).findall(strultp)
        get2 = ''.join(get1)
        return get2.split(";")

    SW = gets(swurl)[0]
    # print(SW)

    SeleaseTime = gets(SeleaseTimeurl)
    # print(SeleaseTime)

    TestTime = gets(TestTimeurl)[0][0:10]
    # print(TestTime)

    TestStop = gets(TestStopurl)[0][0:10]
    # print(TestStop)

    SasePassRate = gets(SasePassRateurl)
    # print(SasePassRate)

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
        # print(Passvalue)

        passrode = passvalue[1].split('=')
        # print(passrode)

        Assigned = passrode[0]
        Assigned_list.append(Assigned)
        # print(Assigned)
        PassRate = passrode[1]
        PassRate_list.append(PassRate)
        # print(PassRate)
        Fail = int(Assigned) - int(Passvalue)
        Fail_list.append(Fail)
        FailRate = str("%.2f" % ((Fail / int(Assigned)) * 100)) + "%"
        # print(str(FailRate) + "%")
        FailRate_list.append(FailRate)

    for i in range(len(urltst)):
        urltst[i] = {'Features': urltst[i], 'Assigned': Assigned_list[i], 'passvalue': passvalue_list[i],
                     'PassRate': PassRate_list[i], 'Fail': Fail_list[i],'FailRate':FailRate_list[i]}


    # 这一部分是在报bug模块
    paht = "/home/pc7/pydjango/djweb/media/648bugweb/newbug/"

    list_bug = os.listdir(paht)
    listad = []
    for i in range(len(list_bug)):
        url = r"file://"+paht+list_bug[i]
        title = "<title>(.*) .*"
        resolution = "<span id=\"resolution-val\" class=\"value .*\".*>\n                                    (.*)\n                                </span>"
        status = ";/span&gt;\">(.*)</span>            </span>"
        Assignee = "</span></span>\n            (.*)\n        </span>"
        bug = ["错误原因:<br>\n(.*)<br>", "错误原因:<br/>\n(.*)<br/>"]
        bug_nub = "发生次数:<br/>\n(.*)<br/>"
        def web(reurl):
            web_source = urllib.request.urlopen(url).read().decode("utf-8")
            return re.compile(reurl).findall(web_source)
        title_value = web(title)
        title_strip = "".join(title_value)
        title_join = title_strip.split(" ")
        bug_value = web(bug[0])
        if len(bug_value) == 0:
            bug_value = web(bug[1])
        Error_Type_value = re.sub(r'Occurred', "", ''.join(bug_value), re.I)
        ID_value = title_join[0].strip("[]")
        Titlee_value = ''.join(title_join[1:])
        Title_value = re.sub(r'-', '', Titlee_value).replace(' ', '')

        liz = ["938", "648"]
        terrace = re.compile(liz[0]).findall(Titlee_value)
        if len(terrace) == 0:
            terrace = re.compile(liz[1]).findall(Titlee_value)
        Terrace = ''.join(terrace)
        status_value = web(status)[0]
        resolution_value = web(resolution)[0]

        Assignee_value = web(Assignee)[0].replace(' ', '')
        occurred_Times = web(bug_nub)
        occurred_times = "".join(occurred_Times)

        lis = [Error_Type_value,ID_value,Title_value,status_value,Assignee_value,resolution_value,occurred_times]
        listad.append(lis)
        opennumber = len(listad)
    for i in range(len(listad)):
        listad[i] = {'Error_Type_value': listad[i][0],'ID_value': listad[i][1], 'Title_value': listad[i][2],
                     'status_value': listad[i][3],'Assignee_value': listad[i][4],
                     'resolution_value': listad[i][5],"occurred_times":listad[i][6]}


    # 这一部分是在old报bug模块
    paht_old = "/home/pc7/pydjango/djweb/media/648bugweb/oldbug/"

    list_bug_old = os.listdir(paht_old)
    listad_old = []


    for i in range(len(list_bug_old)):
        url_old = r"file://" + paht_old + list_bug_old[i]
        title_old = "<title>(.*) .*"
        resolution_old = "<span id=\"resolution-val\" class=\"value .*\".*>\n                                    (.*)\n                                </span>"
        status_old = ";/span&gt;\">(.*)</span>            </span>"
        Assignee_old = "</span></span>\n            (.*)\n        </span>"
        bug_old = ["错误原因:<br>\n(.*)<br>" , "错误原因:<br/>\n(.*)<br/>"]
        bug_nub_old = "发生次数:<br/>\n(.*)<br/>"
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
        Title_value_old = re.sub(r'-' , '' , Titlee_value_old).replace(' ', '')
        status_value_old = web(status_old)[0]
        resolution_value_old = web(resolution_old)[0]
        Assignee_value_old = web(Assignee_old)[0].replace(' ' , '')
        occurred_Times_old = web(bug_nub_old)
        occurred_times_old = "".join(occurred_Times_old)

        lis_old = [Error_Type_value_old , ID_value_old , Title_value_old , status_value_old , Assignee_value_old , resolution_value_old,occurred_times_old]
        listad_old.append(lis_old)

    for i in range(len(listad_old)):
        listad_old[i] = {'Error_Type_value_old': listad_old[i][0] , 'ID_value_old': listad_old[i][1] , 'Title_value_old': listad_old[i][2],
                     'status_value_old': listad_old[i][3], 'Assignee_value_old': listad_old[i][4],
                         'resolution_value_old': listad_old[i][5],'occurred_times_old':listad_old[i][6]}

    if request.method == 'POST':
        openNumber = request.POST.get('openNumber', None)
        closeNumber = request.POST.get('closeNumber' , None)
        urgency = request.POST.get('urgency', None)
        highNumber = request.POST.get('highNumber' , None)
        ordinaryNumber = request.POST.get('ordinaryNumber' , None)
        minorNumber = request.POST.get('minorNumber' , None)
        noNumber = request.POST.get('noNumber', None)
        with open('notet', 'w+')as f:
            f.write(openNumber+'\n'+closeNumber+'\n'+urgency+'\n'+highNumber+'\n'+ordinaryNumber+'\n'+minorNumber+'\n'+noNumber)
    with open('notet', 'r+') as f:
        bgnumber = f.readlines()

    openNumber = bgnumber[0]
    closeNumber = bgnumber[1]
    urgency = bgnumber[2]
    highNumber = bgnumber[3]
    ordinaryNumber = bgnumber[4]
    minorNumber = bgnumber[5]
    noNumber = bgnumber[6]
    return render(request, 'ms648reportok.html', locals())

def reportForm(request):
    lip = []
    for i in range(20):
        lip.append(i)
    return render(request, 'reportForm.html', locals())


def StressTestReport_Demeter(request):
    get938_id = request.GET.get('id')
    return render(request, 'Mstar6A938/'+get938_id)


def StressTestReport_Hera(request):
    get648_id = request.GET.get('id')
    return render(request, 'Mstar6A648/'+get648_id)

def reportrecord938(request):
    # pw = os.path.dirname(os.getcwd())
    #
    # pwz = pw + '/djweb/media/938bugweb/newbug/'
    # listpw = os.listdir(pwz)

    pwt = os.path.dirname(os.getcwd())
    # print(pwt)
    pwzt = pwt + '/djweb/templates/Mstar6A938/'
    listpwt = os.listdir(pwzt)
    # print(listpwt)

    if request.method == 'POST':
        wefile = request.POST.get('name')
        # print(wefile)
        pt = os.getcwd()+'/templates/Mstar6A938/'+wefile
        if os.path.exists(pt):
            os.remove(pt)
    return render(request, 'reportrecord938.html', locals())

def reportrecord(request):
    pw = os.path.dirname(os.getcwd())
    pwx = pw + '/djweb/templates/Mstar6A648/'
    listpx = os.listdir(pwx)

    if request.method == 'POST':
        wefile = request.POST.get('name')
        # print(wefile)
        pt = os.getcwd()+'/templates/Mstar6A648/'+wefile
        if os.path.exists(pt):
            os.remove(pt)
    return render(request, 'reportrecord.html', locals())





def record938(request):
    if request.method == 'POST':
        img = request.FILES['record938']
        imgname = '%s/%s' % (settings.MEDIA_ROOT +'/938bugweb'+'/report', img.name)
        with open(imgname, 'wb')as f:
            for fimg in img.chunks():
                f.write(fimg)
        pw = os.popen('pwd').read()
        shutil.move(imgname, pw.rstrip()+'/templates/Mstar6A938/')
        return HttpResponse('上传成功')
    else:
        return HttpResponse('没有上传成功')




def record648(request):
    if request.method == 'POST':
        img = request.FILES['record648']
        imgname = '%s/%s' % (settings.MEDIA_ROOT +'/648bugweb'+'/report', img.name)
        with open(imgname, 'wb')as f:
            for fimg in img.chunks():
                f.write(fimg)
        pw = os.popen('pwd').read()
        shutil.move(imgname, pw.rstrip()+'/templates/Mstar6A648/')
        return HttpResponse('上传成功')
    else:
        return HttpResponse('没有上传成功')


def student(request):
    if request.method == 'POST':
        t = request.POST.get('name')
        print(t)
    return render(request, 'student.html', locals())

def st1(request):
    if request.method == 'POST':
        t = request.POST.get('name')
        print(t)
        # img = request.FILES['test']
        # print(img)
        return HttpResponse('上传成功')
    else:
        return HttpResponse('没有上传成功')




def ms938reportok(request):
    ulr = r"file:///home/pc7/pydjango/djweb/media/938bugweb/LeTV STRESS Report.html"

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

    swurl = "SW;(.*);Release Time"

    SeleaseTimeurl = 'Release Time;(.*);Test Start Time'

    TestTimeurl = 'Test Start Time;(.*);Test Stop Time'

    TestStopurl = 'Test Stop Time;(.*);Test Total Execution Time'

    SasePassRateurl = 'Case Pass Rate;(.*);<span class="passCount">STRESS Value</span>;'

    def gets(args):
        get1 = re.compile(args).findall(strultp)
        get2 = ''.join(get1)
        return get2.split(";")

    SW = gets(swurl)[0]
    # print(SW)

    SeleaseTime = gets(SeleaseTimeurl)
    # print(SeleaseTime)

    TestTime = gets(TestTimeurl)[0][0:10]
    # print(TestTime)

    TestStop = gets(TestStopurl)[0][0:10]
    # print(TestStop)

    SasePassRate = gets(SasePassRateurl)
    # print(SasePassRate)

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
        # print(Passvalue)

        passrode = passvalue[1].split('=')
        # print(passrode)

        Assigned = passrode[0]
        Assigned_list.append(Assigned)
        # print(Assigned)
        PassRate = passrode[1]
        PassRate_list.append(PassRate)
        # print(PassRate)
        Fail = int(Assigned) - int(Passvalue)
        Fail_list.append(Fail)
        FailRate = str("%.2f" % ((Fail / int(Assigned)) * 100)) + "%"
        # print(str(FailRate) + "%")
        FailRate_list.append(FailRate)

    for i in range(len(urltst)):
        urltst[i] = {'Features': urltst[i] , 'Assigned': Assigned_list[i] , 'passvalue': passvalue_list[i] ,
                     'PassRate': PassRate_list[i] , 'Fail': Fail_list[i] , 'FailRate': FailRate_list[i]}

    # 这一部分是在报bug模块
    paht = "/home/pc7/pydjango/djweb/media/938bugweb/newbug/"

    list_bug = os.listdir(paht)
    listad = []
    for i in range(len(list_bug)):
        url = r"file://" + paht + list_bug[i]
        title = "<title>(.*) .*"
        resolution = "<span id=\"resolution-val\" class=\"value .*\".*>\n                                    (.*)\n                                </span>"
        status = ";/span&gt;\">(.*)</span>            </span>"
        Assignee = "</span></span>\n            (.*)\n        </span>"
        bug = ["错误原因:<br>\n(.*)<br>" , "错误原因:<br/>\n(.*)<br/>"]
        bug_nub = "发生次数:<br/>\n(.*)<br/>"

        def web(reurl):
            web_source = urllib.request.urlopen(url).read().decode("utf-8")
            return re.compile(reurl).findall(web_source)

        title_value = web(title)
        title_strip = "".join(title_value)
        title_join = title_strip.split(" ")
        bug_value = web(bug[0])
        if len(bug_value) == 0:
            bug_value = web(bug[1])
        Error_Type_value = re.sub(r'Occurred' , "" , ''.join(bug_value) , re.I)
        ID_value = title_join[0].strip("[]")
        Titlee_value = ''.join(title_join[1:])
        Title_value = re.sub(r'-' , '' , Titlee_value).replace(' ' , '')

        liz = ["938" , "648"]
        terrace = re.compile(liz[0]).findall(Titlee_value)
        if len(terrace) == 0:
            terrace = re.compile(liz[1]).findall(Titlee_value)
        Terrace = ''.join(terrace)
        status_value = web(status)[0]
        resolution_value = web(resolution)[0]

        Assignee_value = web(Assignee)[0].replace(' ' , '')
        occurred_Times = web(bug_nub)
        occurred_times = "".join(occurred_Times)

        lis = [Error_Type_value , ID_value , Title_value , status_value , Assignee_value , resolution_value ,
               occurred_times]
        listad.append(lis)
        opennumber = len(listad)
    for i in range(len(listad)):
        listad[i] = {'Error_Type_value': listad[i][0] , 'ID_value': listad[i][1] , 'Title_value': listad[i][2] ,
                     'status_value': listad[i][3] , 'Assignee_value': listad[i][4] ,
                     'resolution_value': listad[i][5] , "occurred_times": listad[i][6]}

    # 这一部分是在old报bug模块
    paht_old = "/home/pc7/pydjango/djweb/media/938bugweb/oldbug/"

    list_bug_old = os.listdir(paht_old)
    listad_old = []

    for i in range(len(list_bug_old)):
        url_old = r"file://" + paht_old + list_bug_old[i]
        title_old = "<title>(.*) .*"
        resolution_old = "<span id=\"resolution-val\" class=\"value .*\".*>\n                                    (.*)\n                                </span>"
        status_old = ";/span&gt;\">(.*)</span>            </span>"
        Assignee_old = "</span></span>\n            (.*)\n        </span>"
        bug_old = ["错误原因:<br>\n(.*)<br>" , "错误原因:<br/>\n(.*)<br/>"]
        bug_nub_old = "发生次数:<br/>\n(.*)<br/>"

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
        occurred_Times_old = web(bug_nub_old)
        occurred_times_old = "".join(occurred_Times_old)

        lis_old = [Error_Type_value_old , ID_value_old , Title_value_old , status_value_old , Assignee_value_old ,
                   resolution_value_old , occurred_times_old]
        listad_old.append(lis_old)

    for i in range(len(listad_old)):
        listad_old[i] = {'Error_Type_value_old': listad_old[i][0] , 'ID_value_old': listad_old[i][1] ,
                         'Title_value_old': listad_old[i][2] ,
                         'status_value_old': listad_old[i][3] , 'Assignee_value_old': listad_old[i][4] ,
                         'resolution_value_old': listad_old[i][5] , 'occurred_times_old': listad_old[i][6]}
    if request.method == 'POST':
        openNumber = request.POST.get('openNumber' , None)
        closeNumber = request.POST.get('closeNumber' , None)
        urgency = request.POST.get('urgency' , None)
        highNumber = request.POST.get('highNumber' , None)
        ordinaryNumber = request.POST.get('ordinaryNumber' , None)
        minorNumber = request.POST.get('minorNumber' , None)
        noNumber = request.POST.get('noNumber', None)
        with open('note','w+')as f:
            f.write(openNumber+'\n'+closeNumber+'\n'+urgency+'\n'+highNumber+'\n'+ordinaryNumber+'\n'+minorNumber+'\n'+noNumber)
    with open('note', 'r+') as f:
        bgnumber = f.readlines()

    openNumber = bgnumber[0]
    closeNumber = bgnumber[1]
    urgency = bgnumber[2]
    highNumber = bgnumber[3]
    ordinaryNumber = bgnumber[4]
    minorNumber = bgnumber[5]
    noNumber = bgnumber[6]
    return render(request,'ms938reportok.html',locals())


def ms648reportResult(request):
    if request.method == 'POST':
        save = request.POST.get("save")
        savename = save.split(' ')[1]
        url = 'http://10.58.81.227:8099/ms648reportok/'
        html1 = urllib.request.urlopen(url).read().decode("utf-8")

        html = re.sub(r'<input type="submit" name="save".*text-align: left">', '', html1)
        savehtml(savename , html)
        pw = os.popen('pwd').read()
        pt = pw.rstrip() + '/templates/Mstar6A648/' + savename + '.html'
        if os.path.exists(pt):
            os.remove(pt)
        shutil.move(pw.rstrip() + '/' + savename + '.html', pw.rstrip() + '/templates/Mstar6A648/')
        return HttpResponse('保存成功')
    else:
        return HttpResponse('没有上传成功')


def savehtml(file_name,file_html):
    with open(file_name.replace('/', '_') + '.html','w+') as f:
        f.write(file_html)


def ms938reportResult(request):
    if request.method == 'POST':
        save = request.POST.get("save")
        savename = save.split(' ')[1]
        url = 'http://10.58.81.227:8099/ms938reportok/'
        html1 = urllib.request.urlopen(url).read().decode("utf-8")
        # print(html1)
        html = re.sub(r'<input type="submit" name="save".*text-align: left">', '', html1)
        savehtml(savename, html)
        pw = os.popen('pwd').read()
        pt = pw.rstrip() + '/templates/Mstar6A938/'+savename + '.html'
        if os.path.exists(pt):
            os.remove(pt)
        shutil.move(pw.rstrip() + '/'+savename + '.html', pw.rstrip() + '/templates/Mstar6A938/')

        return HttpResponse('保存成功')
    else:
        return HttpResponse('没有上传成功')