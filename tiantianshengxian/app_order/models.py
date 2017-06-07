# coding:utf-8
from django.db import models
from app_user.models import User
from app_cart.models import CartInfo
from app_goods.models import GoodsInfo

# Create your models here.
class OrderInfo(models.Model):
    oid = models.IntegerField()  # 订单编号
    ouser = models.ForeignKey(User)
    odate = models.DateTimeField()
    opay_way = models.CharField(max_length=30)
    is_paid = models.BooleanField(default=False)
    oaddress = models.CharField(max_length=100)


class OrderDetail(models.Model):
    goid = models.ForeignKey(GoodsInfo)
    count = models.IntegerField()
    order = models.ForeignKey(OrderInfo)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # 订单总共的价格


