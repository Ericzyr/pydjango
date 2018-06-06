#!/usr/bin/env python3
# -*-coding:utf-8-*-
from django.shortcuts import render
from webapp import models
from django.contrib.auth import authenticate,login
# Create your views here.

def homeage(request):
    if request.method=='POST':
        models.wesheet.objects.create(user=user_name , pwd=pass_word)
        if user_name =='root'and pass_word =='pass':
            return render(request, 'homeage.html',{"SW":t.SW ,"testresult":t.phoneData , "totalANR": t.dataANR , "totalTombstone": t.dataTB ,
             "totalFC": t.dataFC , "totalReset": t.dataReset , "totalExeTime": t.totalExeTime ,
             "totalError": t.totalError , "totalcasePass": t.dataPass , "totalcaseExce": t.dataExce ,
             "passRate": t.passRate , "mtbfValue": t.mtbfVal})
