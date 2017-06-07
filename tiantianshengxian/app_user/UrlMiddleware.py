#coding:utf-8
from django.http import HttpResponse,HttpRequest,JsonResponse
from django.shortcuts import redirect
# from django.middleware.csrf import CsrfViewMiddleware
# 上面引进的东西是啥?

# 配合装饰器用的中间件
# class url(object):
#     def process_response(self, request, response):
#         url_list = [
#             '/user/register/',
#             '/user/register_yz/',
#             '/user/register_exist/',
#             '/user/login/',
#             '/user/login_yz/',
#             '/user/logout/',
#         ]
#         if not request.is_ajax() and request.path not in url_list:
#             response.set_cookie('red_url', request.get_full_path())
#         return response

    #  下面是增加测试的代码
    #  中间件用时需要注意: request 跟 response 传入的参数不同
class url(object):

    def process_response(self, request, response):
        url_list = [
            '/user/register/',
            '/user/register_yz/',
            '/user/register_exist/',
            '/user/login/',
            '/user/login_yz/',
            '/user/logout/',
        ]
        if not request.is_ajax() and request.path not in url_list:
            response.set_cookie('red_url', request.get_full_path())
        return response

    def process_request(self, request):
        url_list = [
            '/user/user_center_info/',
            '/user/user_center_site/',
            '/user/user_center_order/',
            '/cart/',
            '/cart/add/',
            '/order/'
        ]
        if request.path in url_list:
            if not request.session.has_key('user_id'):
                if request.is_ajax():
                    return JsonResponse({'is_login':1})
                return redirect('/user/login/')