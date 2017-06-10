from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.cart),
    url('^add/', views.add),
    url('^change/', views.change),
    url('^delete/', views.delete),
]