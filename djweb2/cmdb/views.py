from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from cmdb import models
from cmdb.models import mystudent

def index(request):

    # models.mystudent.objects.create(name='lili',age='15',sex='nv',address='shanghai') #这是对数据库的增加

    empt = models.mystudent.objects.values_list()

    for emps in iter(empt):
        return render(request, 'index.html',{'emps':emps,'empt':empt})