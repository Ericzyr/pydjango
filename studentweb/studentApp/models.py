from django.db import models

# Create your models here.

class studentsheet(models.Model):
    user = models.CharField(max_length=20)
    password = models.CharField(max_length=5)
