#coding:utf-8
from django.shortcuts import render

# Create your views here.
def place_order(request):

    context = {'title':'我的订单'}
    return render(request,'app_order/place_order.html',context)