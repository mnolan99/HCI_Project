from django.conf.urls import url
from ontrack_app import views

#the urls for all of the pages on the web app
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^search/', views.search, name='search'),
    url(r'^restaurant/', views.restaurant, name='restaurant'),
    url(r'^onCampus/', views.onCampus, name='onCampus'),
    url(r'^offCampus/', views.offCampus, name='offCampus'),
    url(r'^page/(?P<page_name_slug>[\w\-]+)/$', views.review, name='review'),
    url(r'^add_review/(?P<page_name_slug>[\w\-]+)/$', views.add_review, name='add_review'), 
    url(r'^about/', views.about, name='about'),
    url(r'^FAQ/', views.FAQ, name='FAQ'),
    url(r'^contact-us/', views.email, name='contact-us'),
    url(r'^t&cs/', views.tAndC, name='t&cs'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^restricted/', views.restricted, name='restricted'),
    url(r'^logout/$', views.user_logout, name='logout'),
     url(r'^email/$', views.email, name='email'),
    url(r'^invalidLogin/$', views.invalidLogin, name='invalidLogin'),
    url(r'^updates/$', views.updates, name='updates'),
    url(r'^appointments/$', views.updates, name='appointments'),


]

