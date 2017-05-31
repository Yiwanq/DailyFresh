# coding:utf-8
from django.conf.urls import url
import views

urlpatterns = [
    url(r'^login/$', views.login),
    url('^register/$', views.register),
    url('^user_center_info/$', views.user_center_info),
]