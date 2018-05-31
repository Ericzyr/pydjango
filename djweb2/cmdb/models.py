from django.db import models

# Create your models here.


'''
django 1.9之后

python manage.py syncdb

改成了
python manage.py makemigrations
python manage.py migrate


或者
python manage.py makemigrations

'''

from django.db import models


#这是建立数据库

class mystudent(models.Model):
    name = models.CharField(max_length=20)
    age = models.CharField(max_length=5)
    sex = models.CharField(max_length=5)
    address = models.CharField(max_length=30)

    # def __unicode__(self):
    #     return self.name
