from django.conf.urls import url
from ontrack_app import views

#the urls for all of the pages on the web app
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
    url(r'^FAQ/', views.FAQ, name='FAQ'),
    url(r'^t&cs/', views.tAndC, name='t&cs'),
    url(r'^register/$', views.register, name='register'),
   url(r'^login/$', views.user_login, name='login'),
    url(r'^restricted/', views.restricted, name='restricted'),
    url(r'^logout/$', views.user_logout, name='logout'),
    #url(r'^invalidLogin/$', views.invalidLogin, name='invalidLogin'),
    url(r'^updates/$', views.updates, name='updates'),
    url(r'^appts/$', views.appts, name='appts'),
     url(r'^symptoms/$', views.symptoms, name='symptoms')
]

