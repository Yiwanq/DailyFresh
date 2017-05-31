# coding: utf-8
from django.db import models

# Create your models here.
class user(models.Model):
    uname = models.CharField(max_length = 20)
    upwd = models.CharField(max_length = 20)
    uemail = models.CharField(max_length = 20)
    uphone = models.CharField(max_length=20)
    uaddress = models.CharField(max_length = 50)
