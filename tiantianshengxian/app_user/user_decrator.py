# coding:utf-8
# from django.shortcuts import redirect
from django.http import HttpResponseRedirect,JsonResponse

def login(inner):
    def log_fun(request,*arg,**kwargs):
        if request.session.has_key('user_id'):
            return inner(request,*arg,**kwargs)
        else:
            if request.is_ajax():
                return JsonResponse({'is_login':1})
            return HttpResponseRedirect('/user/login/')
            # red.set_cookie('url', request.get_full_path())
            # return red
    return log_fun

'''
http://127.0.0.1:8080/200/?type=10
request.path：表示当前路径，为/200/
request.get_full_path()：表示完整路径，为/200/?type=10

'''