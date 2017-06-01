# coding:utf-8
from django.conf.urls import url
import views

urlpatterns = [
    url('^login/$', views.login),
    url('^login_yz/$', views.login_yz),
    url('^login_out/$', views.login_out),
    url('^register/$', views.register),
    url('^user_center_info/$', views.user_center_info),
    url('^user_center_order/$', views.user_center_order),
    url('^user_center_site/$', views.user_center_site),
    url('^register_yz/$', views.register_yz),
    url('^register_exist/$', views.register_exist),
]