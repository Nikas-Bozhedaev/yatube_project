# posts/urls.py
from django.urls import path

from django.conf.urls import url

from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='index'),
    #path('group/<slug:slug>', views.group_posts, name='group_posts')
    #url(r'^group/(?P<slug>[-a-zA-Z0-9_]+)/$', views.group_posts, name='group_posts')
] 