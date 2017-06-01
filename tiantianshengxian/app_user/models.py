# coding: utf-8
from django.db import models

# Create your models here.
class User(models.Model):
    uname = models.CharField(max_length = 20)
    upwd = models.CharField(max_length = 50)
    uemail = models.CharField(max_length = 20)
    uphone = models.CharField(max_length=20)
    uaddress = models.CharField(max_length = 50)
    ushou = models.CharField(max_length = 20, blank= False, null=False)
