#coding:utf-8
from django.shortcuts import redirect
from django.shortcuts import render
from app_user.models import User
from app_goods.models import GoodsInfo
from app_cart.models import CartInfo
from django.db import transaction
from models import *
from datetime import datetime

# Create your views here.
def place_order(request):  # 有些多余,因为用一个 views 就可以完成
    cartid = request.GET.getlist('cartid')
    userid = request.session.get('user_id')
    user = User.objects.get(id=userid)
    carts = CartInfo.objects.filter(id__in = cartid)

    context = {'title':'我的订单','user':user, 'carts':carts}
    return render(request,'app_order/place_order.html',context)

@transaction.atomic
def order_handle(request):
    # 判断仓库 → 减少库存 → 创建订单 → 创建详单 → 删除购物车
    post = request.POST
    cartid = post.getlist('cartid')
    address = post.get('address')
    pay = post.get('pay_style')
    user = request.session.get('user_id')
    tran_id = transaction.savepoint()

    # try:
    #     # carts = CartInfo.objects.filter(id__in = cartid) # cartid 是 unicode 编码的数值列表
    #     # 创建订单
    #     order = OrderInfo()
    #     now = datetime.now()
    #     order.oid = '%s%d' %( now.strftime('%Y%m%d%H%M%S'), user )
    #     order.odate = now
    #     order.opay_way = pay
    #     order.oaddress = address
    #     order.oprice = 0
    #     order.is_paid = False
    #     order.ouser = User.objects.get(id=user)
    #     order.save()
    #
    #     # 应该在购物车栏判断为空
    #     total = 0
    #     for id in cartid:
    #         cart = CartInfo.objects.get(pk=id)
    #         kucun = cart.good.gkucun
    #
    #         if cart.count > kucun:
    #             transaction.savepoint_rollback(tran_id)
    #             return redirect('/cart/')
    #         else:
    #             # 减少库存
    #             cart.good.gkucun = kucun - cart.count
    #             cart.good.save()
    #
    #             # 购物车删除
    #             cart.delete()
    #
    #             # 创建详单
    #             detail = OrderDetail()
    #             detail.goid = cart.good  # 外键相连,也要赋值
    #             detail.count = cart.count
    #             detail.order = order
    #             detail.price = cart.good.gprice
    #             total += cart.count * cart.good.gprice
    #             detail.save()
    #
    #     order.oprice = total
    #     order.save()
    #     transaction.savepoint_commit(tran_id)
    #     return redirect('/user/user_center_order/')
    # except:
    #     transaction.savepoint_rollback(tran_id)
    #     return redirect('/goods/')

    try:
        carts = CartInfo.objects.filter(id__in = cartid) # cartid 是 unicode 编码的数值列表

        # 应该在购物车栏判断为空
        total = 0

        # 创建订单
        order = OrderInfo()
        now = datetime.now()
        order.oid = '%s%d' % (now.strftime('%Y%m%d%H%M%S'), user)
        order.odate = now
        order.opay_way = pay
        order.oaddress = address
        order.oprice = 0
        order.is_paid = False
        order.ouser = User.objects.get(id=user)
        order.save()
        for cart in carts:
            # cart = CartInfo.objects.get(pk=id)
            kucun = cart.good.gkucun

            if cart.count > kucun:
                transaction.savepoint_rollback(tran_id)
                return redirect('/cart/')
            else:
                # 减少库存
                cart.good.gkucun = kucun - cart.count
                cart.good.save()

                # 购物车删除
                cart.delete()

                # 创建详单
                detail = OrderDetail()
                detail.goid = cart.good  # 外键相连,也要赋值
                detail.count = cart.count
                detail.order = order
                detail.price = cart.good.gprice
                total += cart.count * cart.good.gprice
                detail.save()

        order.oprice = total
        order.save()
        transaction.savepoint_commit(tran_id)
        return redirect('/user/user_center_order/')
    except:
        transaction.savepoint_rollback(tran_id)
        return redirect('/cart/')

def pay(request):

    return redirect('/user/user_center_order/')