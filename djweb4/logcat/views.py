from django.shortcuts import render

def home(request):
    return render(request,'home.html',{"SW":"我是中国人hell"})






