from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.test, name='test'),
    url(r'^send/$', views.send, name='send'),
    url(r'^receive/$', views.receive, name='receive'),
    url(r'^sync/$', views.sync, name='sync'),
    url(r'^join/$', views.join, name='join'),
    url(r'^leave/$', views.leave, name='leave')
]