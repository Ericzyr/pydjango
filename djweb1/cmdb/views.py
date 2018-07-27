
from django.shortcuts import render
from django.http import FileResponse
from cmdb import models
from django.template import loader,context
from django.shortcuts import HttpResponse

# Create your views here
def index(request):
    return render(request, "index.html",locals())

def student(request):
    if request.method == 'POST':
        namet = request.POST.get('name')
        with open('note','w+')as f:
            f.write(namet)
    with open('note','r+')as f:
        name = f.readlines()[0]
    return render(request, "student.html", locals())

def download(request):
    file = open('static_model/css/xlsx_file.xlsx', 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="xlsx_file.xlsx"'
    return response
