from django.conf.urls import url
import views

urlpatterns = [
    url('^$', views.index),
    url('^detail(\d+)/', views.detail),
    url('^list(\d+)/', views.list),
    url('^search/', views.search),
]