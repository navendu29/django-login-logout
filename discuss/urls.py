from django.conf.urls import url

from . import views

app_name = 'discuss'
urlpatterns = [

    #   url(r'^$',views.index,name='index'),
    url(r'^$',views.register, name='register'),
    url(r'^login/$', views.login, name='log'),

]