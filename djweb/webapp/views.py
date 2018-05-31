from django.shortcuts import render
from webapp import models
from django.contrib.auth import authenticate,login
# Create your views here.

def desktop(request):
    return render(request,'desktop.html')

def index(request):
    return render(request , 'index.html')

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
            return render(request, 'homeage.html',{'us':user_name,'pa':pass_word})
