from django.conf.urls import patterns, url
from checkList import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^register/', views.register, name='register'),
                       url(r'^about/', views.about, name='about'),
                       url(r'^login/$', views.user_login, name='login'),
                       url(r'^logout/$', views.user_logout, name='logout'),
                       url(r'^edit/$', views.user_edit, name='edit'),
                       url(r'^list/$', views.list, name='list'),
                       )
