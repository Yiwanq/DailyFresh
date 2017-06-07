# coding:utf-8
from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from app_goods import models
from app_user import models, user_decrator
from models import *


# Create your views here.
# @user_decrator.login
def cart(request):
    carts = CartInfo.objects.filter(user_id=request.session['user_id'])
    context = {'title':'我的购物车', 'carts':carts}
    return render(request, 'app_cart/cart.html', context)

# @user_decrator.login
def add(request):
    user_id = request.session['user_id']
    good_id = request.GET.get('good','1')
    num = request.GET.get('count','1')
    cart = CartInfo.objects.filter(user_id=int(user_id)).filter(good_id=int(good_id))
    if len(cart) == 0:
        cart = CartInfo()  # 表示一条记录,需要根据user_id  good_id 得到具体的商品
        cart.count = int(num)
    else:
        cart = cart[0]
        cart.count = cart.count + int(num)

    cart.user_id = user_id
    cart.good_id = good_id
    cart.save()

    if request.is_ajax():
        return JsonResponse({'goods_num':CartInfo.objects.filter(user_id=user_id).count()})
    else:
        # return HttpResponse('ok')
        return redirect('/cart/')  # 应该出现加入购物车的提示面,是否需要继续购物,不能直接返回购物车

def change(request):
    id = int(request.GET.get('id'))
    count = int(request.GET.get('count'))
    carts = CartInfo.objects.filter(id=id)
    if len(carts) > 0:
        carts[0].count = count
        carts[0].save()  # 修改其属性,需要调用save()数据库方法
    return JsonResponse({})

def delete(request):
    id = int(request.GET.get('id'))
    carts = CartInfo.objects.filter(id=id)
    if len(carts) > 0:
        print 'dfs'
        carts[0].delete()  # delete() 本身是调用数据库的方法,不需要save()
        # carts[0].save()
    return JsonResponse({})
