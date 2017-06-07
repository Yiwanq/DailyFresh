# coding:utf-8
from django.shortcuts import render,redirect
from django.http import JsonResponse, HttpResponseRedirect
from models import User
from hashlib import sha1
import user_decrator
from app_goods.models import *
from app_cart.models import *

# Create your views here.
def login(request):
    uname = request.COOKIES.get('uname','')
    context = {'title':'登录', 'error_name':0, 'error_pwd':0, 'uname':uname}
    return render(request, 'app_user/login.html',context)

def login_yz(request):
    info = request.POST
    uname = info.get('username')
    upwd = info.get('pwd')
    jizhu = info.get('jizhu', 0)  # 值可以取到

    users = User.objects.filter(uname=uname) # filter 是集合
    print users  # 数据库用户也可以取到
    if len(users) == 1:
        s01 = sha1()
        s01.update(upwd)
        print s01.hexdigest()
        if users[0].upwd == s01.hexdigest():

            url = request.COOKIES.get('red_url','/user/user_center_info/') # 记住用户上次的页面
            red = HttpResponseRedirect(url) # 重新定向
            red.set_cookie('red_url','',max_age=-1)
            if jizhu == 0:
                red.set_cookie('uname','',max_age=-1)
            else:
                red.set_cookie('uname', uname)
            request.session['user_id'] = users[0].id
            request.session['user_name'] = uname
            return red
        else:
            context = {'title':'登录', 'error_name':0, 'error_pwd':1,'uname':uname,'upwd':upwd}
            return render(request,'app_user/login.html',context)
    else:
        context = {'title': '登录', 'error_name': 1, 'error_pwd': 0, 'uname': uname, 'upwd': upwd}
        return render(request, 'app_user/login.html', context)

def logout(request):
    request.session.flush()
    return redirect('/goods/')

def register(request):
    return render(request, 'app_user/register.html', {'title':'注册'})

def register_yz(request):
    info =request.POST
    uname = info.get('user_name')
    upwd = info.get('pwd')
    uemail = info.get('email')

    s01 = sha1()
    s01.update(upwd)
    upwd2 = s01.hexdigest()

    user = User()
    user.uname = uname
    user.upwd = upwd2
    user.uemail = uemail
    user.save()
    return redirect('/user/login/')

def register_exist(request):
    uname = request.GET.get('name')
    num = User.objects.filter(uname = uname)
    num = num.count()
    return JsonResponse({'num':num})

# @user_decrator.login
def user_center_info(request):
    uid = request.session.get('user_id')
    user = User.objects.filter(pk = uid)
    uname = user[0].uname
    uaddress = user[0].uaddress
    uphone = user[0].uphone
    uemail = user[0].uemail

    li = request.COOKIES.get('liulan','')
    liulan = li.split(',')
    glist = []
    if liulan != ['']:
        print liulan
        for i in liulan:
            goods = GoodsInfo.objects.filter(pk = int(i))
            glist.append(goods[0])
    goods_num = CartInfo.objects.filter(user_id=uid).count()
    context={'title':'用户中心','uname':uname ,'uaddress':uaddress,'uphone':uphone,'uemail':uemail,'glist':glist,'goods_num':goods_num}
    return render(request, 'app_user/user_center_info.html',context)

# @user_decrator.login
def user_center_order(request):
    goods_num = CartInfo.objects.filter(user_id=request.session.get('user_id')).count()
    context = {'title': '用户中心','goods_num':goods_num}
    return render(request, 'app_user/user_center_order.html',context)

# @user_decrator.login
def user_center_site(request):
    # 先在数据库中读取数据,再获取 POST 数据 填充 user 信息
    user = User.objects.get(pk = request.session['user_id'])
    print user
    if request.method == 'POST':
        post = request.POST
        user.ushou = post.get('ushou')
        user.uaddress = post.get('uaddress')
        user.uphone = post.get('uphone')
        user.uemail = post.get('uemail')
        user.save()
    goods_num = CartInfo.objects.filter(user_id=request.session.get('user_id')).count()
    context = {'title': '用户中心', 'user': user,'goods_num':goods_num}
    return render(request, 'app_user/user_center_site.html',context)












