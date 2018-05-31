
from django.shortcuts import render
from cmdb import models
from django.template import loader,context
from django.shortcuts import HttpResponse

# Create your views here.

user_list = [
    {'user': "jack","pwd":"adc"},
    {'user': "tom","pwd":"Adc"},
]


class student_class(object):
    def __init__(self, name, age, sex):
        self.Name = name
        self.Age = age
        self.Sex = sex
    def scholl(self):
        return '{} go scholl'.format(self.Name)

student = student_class('jack', '24', '男')

stud_list = ['python', 'shell', 'java']

class school(student_class):
    def __init__(self,name,age,sex,grade):
        super(school, self).__init__(name,age,sex)
        self.Grade = grade
    def goto(self,args):
        return '{} go to school {}'.format(self.Name,args)




student1=school('Heren','25','女','一（二）班')


s2 = student1.goto('beijing')





def index(request):


    if request.method == "POST":
        # username = request.get_host("username", None)
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        # print(username,password)
        # temp = {"user": username,"pwd": password}
        # user_list.append(temp)
    # return HttpResponse("hell world,你好，世界")
        models.UserInfo.objects.create(user=username, pwd=password)

    user_list = models.UserInfo.objects.all()
    return render(request, "index.html",
                  {"data": user_list,
                   "title": "Welocme to Beijing",
                   "student": student,
                   'list': stud_list,
                   })


# def index1(request):
#     t = loader.get_template(index1())
#     c = context({'uname':'alen'})
#     return HttpResponse(t.render(c))



def index1(request):
    return render(request, 'index1.html', {'name':'alen','s2':s2})