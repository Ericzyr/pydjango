from django.db import models
# Create your models here.
class UserInfo(models.Model):
    user = models.CharField(max_length=32)
    pwd = models.CharField(max_length=32)


# class Employeee(models.Model):
#     name = models.CharField(max_length=20)



'''
django 1.9之后

python manage.py syncdb

改成了
python manage.py makemigrations
python manage.py migrate


或者
python manage.py makemigrations

'''




# from django.db import models
#
# class Employee(models.Model):
#      name=models.CharField(max_length=20)