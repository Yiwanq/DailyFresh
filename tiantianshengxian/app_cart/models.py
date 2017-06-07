#coding:utf-8
from django.db import models
from app_user.models import User
from app_goods.models import GoodsInfo

# Create your models here.
class CartInfo(models.Model):
    good = models.ForeignKey(GoodsInfo)
    user = models.ForeignKey(User)
    count = models.IntegerField()