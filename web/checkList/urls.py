from django.conf.urls import patterns, url
from checkList import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^register/', views.register, name='register'), # ADD NEW PATTERN!,
        url(r'^about/', views.about, name='about'),
        url(r'^login/$', views.user_login, name='login'),
        url(r'^logout/$', views.user_logout, name='logout'),
        )