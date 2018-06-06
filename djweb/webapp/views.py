from django.shortcuts import render
from webapp import models
from django.contrib.auth import authenticate,login
# Create your views here.

def desktop(request):
    return render(request,'desktop.html')

def index(request):
    return render(request , 'index.html')


def getFolderList(folder):
    pList = []
    for f in os.listdir(folder):
        if os.path.isdir(os.path.join(folder , f)):
            pList.append(os.path.join(folder , f))
    pList.sort(key=lambda x: os.stat(x).st_ctime)
    return pList


def getLoopData(logFolder , loopC):
    caseLogList = []
    for folder in os.listdir(logFolder):
        if os.path.isdir(os.path.join(logFolder , folder)):
            caseLogList.append(os.path.join(logFolder , folder))
    caseLogList.sort(key=lambda x: os.stat(x).st_ctime)
    _p = LogParser(4 , caseLogList)
    return _p


def getBuildInfo(folder):
    try:
        phoneInfo = open(folder + "/phoneInfo.txt" , "r")
        lines = phoneInfo.readlines()
    except IOError as e:
        lines = ""
    phoneVer = ""
    phoneIMEI = ""
    phoneDate = ""
    startTime = ""
    endTime = ""
    phoneExeTime = 0
    for line in lines:
        if line.find("buildVersion==") != -1:  # get build version
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
    startDateTime = datetime.strptime(startTime , "%Y-%m-%d %H:%M:%S")
    endDateTime = datetime.strptime(endTime , "%Y-%m-%d %H:%M:%S")
    phoneExeTime = (endDateTime - startDateTime).total_seconds() / 3600
    phoneExeTime = round(phoneExeTime , 1)
    return phoneVer , phoneIMEI , phoneDate , startTime , endTime , phoneExeTime


def main(argv):
    rootFolder1 = argv[1]
    rootFolder = "apptest_TV"
    # 	rootFolder = "/home/lihb/MTBF_For_Phone/20141022"
    # test phone numbers
    phoneList = getFolderList(rootFolder)
    # 	print phoneList
    phoneDataList = []
    phoneC = 0
    phoneFC = 0
    phoneTB = 0
    phoneReset = 0
    phoneANR = 0
    Pass = 0
    Exce = 0
    rate = 0
    casePass = 0
    caseExce = 0
    totalcasePass = 0
    totalcaseExce = 0
    totalFC = 0
    totalTB = 0
    totalANR = 0
    totalReset = 0
    totalExeTime = 0
    totalError = 0
    for phone in phoneList:
        phoneFC = 0
        phoneTB = 0
        phoneReset = 0
        phoneANR = 0
        casePass = 0
        caseExce = 0
        Pass = 0
        Exce = 0
        rate = 0
        phoneC += 1
        # phone test loops
        # cPhone = "Phone" + str(phoneC)  # current phone key
        cPhone = phone.split("/")[-1]
        loopList = getFolderList(phone)
        #  		print loopList
        loopC = 0
        loopDataList = []
        for loop in loopList:
            loopC += 1
            cLoopData = getLoopData(loop , loopC)
            loopDataList.append({'loopName': "loop" + str(loopC) , 'loopData': cLoopData.getResultData()})
            phoneFC += cLoopData.summarySheet['fc']
            phoneTB += cLoopData.summarySheet['tb']
            phoneANR += cLoopData.summarySheet['anr']
            phoneReset += cLoopData.summarySheet['reset']
            casePass += cLoopData.summarySheet['pass']
            caseExce += cLoopData.summarySheet['exed']
        Pass = casePass
        Exce = caseExce
        rate = '%.2f' % (casePass / caseExce * 100)
        phoneVer , phoneIMEI , phoneDate , phoneStartTime , phoneEndTime , phoneExeTime = getBuildInfo(
            rootFolder + "/" + cPhone)
        phoneDataList.append({'phoneName': cPhone ,
                              'summary': {"buildDate": phoneDate , "release": phoneVer , "IMEI": phoneIMEI ,
                                          "startTime": phoneStartTime , "EndTime": phoneEndTime ,
                                          "exeTime": str(phoneExeTime) + "Hrs" , "ANR": phoneANR , "FC": phoneFC ,
                                          "Tombstone": phoneTB , "Reset": phoneReset , "Pass": Pass , "Exce": Exce ,
                                          "Rate": rate} , 'phoneData': loopDataList})
        totalcasePass += casePass
        totalcaseExce += caseExce
        totalFC += phoneFC
        totalTB += phoneTB
        totalANR += phoneANR
        totalReset += phoneReset
        totalExeTime += phoneExeTime
        totalError = totalFC + totalTB + totalANR + totalReset
    # 	HtmlReport(phoneDataList).writeToFile(os.path.dirname(__file__))
    if totalError > 0:
        mtbfVal = totalExeTime / totalError
    else:
        mtbfVal = totalExeTime / 1
    mtbfVal = round(mtbfVal , 1);
    passRate = '%.2f' % (totalcasePass / totalcaseExce * 100)
    HtmlReport(phoneDataList , totalFC , totalTB , totalANR , totalReset , str(totalExeTime) + "Hrs" , totalError ,
               totalcasePass , totalcaseExce , passRate , mtbfVal).writeToFile(rootFolder)


def main(argv):
    rootFolder1 = argv[1]
    rootFolder = "apptest_TV"
    # 	rootFolder = "/home/lihb/MTBF_For_Phone/20141022"
    # test phone numbers
    phoneList = getFolderList(rootFolder)
    # 	print phoneList
    phoneDataList = []
    phoneC = 0
    phoneFC = 0
    phoneTB = 0
    phoneReset = 0
    phoneANR = 0
    Pass = 0
    Exce = 0
    rate = 0
    casePass = 0
    caseExce = 0
    totalcasePass = 0
    totalcaseExce = 0
    totalFC = 0
    totalTB = 0
    totalANR = 0
    totalReset = 0
    totalExeTime = 0
    totalError = 0
    for phone in phoneList:
        phoneFC = 0
        phoneTB = 0
        phoneReset = 0
        phoneANR = 0
        casePass = 0
        caseExce = 0
        Pass = 0
        Exce = 0
        rate = 0
        phoneC += 1
        # phone test loops
        # cPhone = "Phone" + str(phoneC)  # current phone key
        cPhone = phone.split("/")[-1]
        loopList = getFolderList(phone)
        #  		print loopList
        loopC = 0
        loopDataList = []
        for loop in loopList:
            loopC += 1
            cLoopData = getLoopData(loop , loopC)
            loopDataList.append({'loopName': "loop" + str(loopC) , 'loopData': cLoopData.getResultData()})
            phoneFC += cLoopData.summarySheet['fc']
            phoneTB += cLoopData.summarySheet['tb']
            phoneANR += cLoopData.summarySheet['anr']
            phoneReset += cLoopData.summarySheet['reset']
            casePass += cLoopData.summarySheet['pass']
            caseExce += cLoopData.summarySheet['exed']
        Pass = casePass
        Exce = caseExce
        rate = '%.2f' % (casePass / caseExce * 100)
        phoneVer , phoneIMEI , phoneDate , phoneStartTime , phoneEndTime , phoneExeTime = getBuildInfo(
            rootFolder + "/" + cPhone)
        phoneDataList.append({'phoneName': cPhone ,
                              'summary': {"buildDate": phoneDate , "release": phoneVer , "IMEI": phoneIMEI ,
                                          "startTime": phoneStartTime , "EndTime": phoneEndTime ,
                                          "exeTime": str(phoneExeTime) + "Hrs" , "ANR": phoneANR , "FC": phoneFC ,
                                          "Tombstone": phoneTB , "Reset": phoneReset , "Pass": Pass , "Exce": Exce ,
                                          "Rate": rate} , 'phoneData': loopDataList})
        totalcasePass += casePass
        totalcaseExce += caseExce
        totalFC += phoneFC
        totalTB += phoneTB
        totalANR += phoneANR
        totalReset += phoneReset
        totalExeTime += phoneExeTime
        totalError = totalFC + totalTB + totalANR + totalReset
    # 	HtmlReport(phoneDataList).writeToFile(os.path.dirname(__file__))
    if totalError > 0:
        mtbfVal = totalExeTime / totalError
    else:
        mtbfVal = totalExeTime / 1
    mtbfVal = round(mtbfVal , 1);
    passRate = '%.2f' % (totalcasePass / totalcaseExce * 100)
    # HtmlReport(phoneDataList , totalFC , totalTB , totalANR , totalReset , str(totalExeTime) + "Hrs" , totalError ,
    #            totalcasePass , totalcaseExce , passRate , mtbfVal).writeToFile(rootFolder)



class student(object):
    def __init__(self,SW,phoneData , dataFC , dataTB , dataANR , dataReset , totalExeTime , totalError , dataPass ,
                 dataExce , passRate , mtbfVal):
        self.SW=SW
        self.phoneData = phoneData
        self.dataFC = dataFC
        self.dataTB = dataTB
        self.dataANR = dataANR
        self.dataPass = dataPass
        self.dataExce = dataExce
        self.dataReset = dataReset
        self.totalExeTime = totalExeTime
        self.totalError = totalError
        self.mtbfVal = mtbfVal
        self.passRate = passRate
t=student("x4-50",2,3,4,5,6,7,8,9,10,11,12)



def homeage(request):
    if request.method=='POST':
        user_name=request.POST.get('username', None)
        pass_word = request.POST.get('password', None)
        # user = authenticate(username=user_name,password=pass_word)
        # if user is not  None:
        #     login(request,user)
        #     return render(request,'homeage.html')

        # else:
        #     return render(request , 'index.html')
        models.wesheet.objects.create(user=user_name , pwd=pass_word)
        if user_name =='root'and pass_word =='pass':
            return render(request, 'homeage.html',{"SW":t.SW ,"testresult":t.phoneData , "totalANR": t.dataANR , "totalTombstone": t.dataTB ,
             "totalFC": t.dataFC , "totalReset": t.dataReset , "totalExeTime": t.totalExeTime ,
             "totalError": t.totalError , "totalcasePass": t.dataPass , "totalcaseExce": t.dataExce ,
             "passRate": t.passRate , "mtbfValue": t.mtbfVal})
