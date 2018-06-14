from django.shortcuts import render
# from studentApp import models
from studentApp import models
from django.contrib.auth import authenticate,login








def gotest(request):
    return render(request, 'gotest.html')


def desktop(request):
    return render(request,'desktop.html')


def login(request):
    return render(request,'login.html',)

def homepage(request):
    if request.method == "POST":
        username = request.POST.get("username", None)
        password = int(request.POST.get("password", None))
        user = authenticate(username = username,password=password)
        if user is not None:
            login(request,user)
            return render(request,'homepage.html',{})
            pass
        else:
            return render(request,'desktop.html',{})


        if username == 'root' and password == 123:
            return render(request, 'homepage.html',)
    elif request.method == "GET":
        return render(request,'login.html')