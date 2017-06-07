# coding:utf-8
from django.shortcuts import render
from models import *
from django.core.paginator import Paginator
from app_cart.models import *

# Create your views here.
def index(request):
    list11 = GoodsInfo.objects.filter(gtype_id=1).order_by('-gclick')[0:3]
    list12 = GoodsInfo.objects.filter(gtype_id=1).order_by('-id')[0:4]
    list21 = GoodsInfo.objects.filter(gtype_id=2).order_by('-gclick')[0:3]
    list22 = GoodsInfo.objects.filter(gtype_id=2).order_by('-id')[0:4]
    list31 = GoodsInfo.objects.filter(gtype_id=3).order_by('-gclick')[0:3]
    list32 = GoodsInfo.objects.filter(gtype_id=3).order_by('-id')[0:4]
    list41 = GoodsInfo.objects.filter(gtype_id=4).order_by('-gclick')[0:3]
    list42 = GoodsInfo.objects.filter(gtype_id=4).order_by('-id')[0:4]
    list51 = GoodsInfo.objects.filter(gtype_id=5).order_by('-gclick')[0:3]
    list52 = GoodsInfo.objects.filter(gtype_id=5).order_by('-id')[0:4]
    list61 = GoodsInfo.objects.filter(gtype_id=6).order_by('-gclick')[0:3]
    list62 = GoodsInfo.objects.filter(gtype_id=6).order_by('-id')[0:4]
    try:
        uid = request.session.get('user_id')
        goods_num = CartInfo.objects.filter(user_id=uid).count()
    except:
        goods_num = 0
    context = {'title':'首页','list11':list11,'list12':list12,
               'list21':list21,'list22':list22,
               'list31':list31,'list32':list32,
               'list41':list41,'list42':list42,
               'list51':list51,'list52':list52,
               'list61':list61,'list62':list62,
               'goods_num':goods_num,'page_num':1}
    return render(request, 'app_goods/index.html', context)

def detail(request,id):
    type_id = GoodsInfo.objects.get(id=int(id)).gtype_id
    list01 = GoodsInfo.objects.filter(gtype_id=type_id).order_by('-id')[0:2]
    good = GoodsInfo.objects.get(id=id)
    good.gclick += 1
    good.save()

    try:
        uid = request.session.get('user_id')
        goods_num = CartInfo.objects.filter(user_id=uid).count()
    except:
        goods_num = 0

    context = {'title': '商品详情','list01':list01,'good':good,'goods_num':goods_num,'page_num':1}
    red = render(request, 'app_goods/detail.html', context)

    li = request.COOKIES.get('liulan','')
    liulan = li.split(',')
    if liulan == ['']:
        red.set_cookie('liulan', id)
    else:
        if id in liulan:
            liulan.remove(id)
        liulan.insert(0, id)
        if len(liulan) >5 :
            liulan.pop()
        liulan2 = ','.join(liulan)
        red.set_cookie('liulan', liulan2)
    return red

def list(request, id):
    order = request.GET.get('order','0')  # 用GET 方法有风险,必须传值
    if order == '1': # 注意:通过get方式传递过来的都是字符串
        type = '-gclick'
    elif order == '2':
        type = '-gprice'
    else:
        type = '-id'
    list01 = GoodsInfo.objects.filter(gtype_id=id).order_by('-id')[0:2]
    list02 = GoodsInfo.objects.filter(gtype_id=id).order_by(type)

    p = request.GET.get('page','1')
    pagenator = Paginator(list02,9)
    page = pagenator.page(int(p))
    if p < 1:
        p = 1
    elif p > pagenator.num_pages:
        p = pagenator.num_pages
    else:
        p = request.GET.get('page', '1')

    try:
        uid = request.session.get('user_id')
        goods_num = CartInfo.objects.filter(user_id=uid).count()
    except:
        goods_num = 0

    context = {'title': '商品列表', 'list01':list01, 'list02':list02, 'page':page,'order':order,'goods_num':goods_num,'page_num':1}
    return render(request, 'app_goods/list.html', context)

def search(request):
    return render(request, 'search/search.html')

