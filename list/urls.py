
from django.conf.urls import url
from .views import *

urlpatterns = [

    url(r'^index/$',listindex,name='index'),
    url(r'^(?P<id>\d+)/$',listdetail,name='detail'),
    url(r'^create/$',listcreate,name='create'),
    url(r'^(?P<id>\d+)/delete/$',listdelete,name='delete'),
    url(r'^istatistik/$', istatistik, name='istatistik'),

]
