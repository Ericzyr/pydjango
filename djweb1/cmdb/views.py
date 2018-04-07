from django.shortcuts import render
from cmdb import models
from django.shortcuts import HttpResponse

# Create your views here.
user_list = [
    {'user': "jack","pwd":"adc"},
    {'user': "tom","pwd":"Adc"},
]



def index(request):

    if request.method == "POST":
        print('true')
        # username = request.get_host("username", None)
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        # print(username,password)
        # temp = {"user": username,"pwd": password}
        # user_list.append(temp)
    # return HttpResponse("hell world,你好，世界")


        models.UserInfo.objects.create(user=username,pwd=password)
    user_list = models.UserInfo.objects.all()


    return render(request, "index.html", {"data": user_list})
