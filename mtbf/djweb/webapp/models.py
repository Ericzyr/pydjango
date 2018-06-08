from django.db import models


class wesheet(models.Model):
    user = models.CharField(max_length=20)
    pwd = models.CharField(max_length=20)


class westudent(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    sex = models.CharField(max_length=2)
    add = models.TextField()