from django.conf.urls import url
from django.urls import path
from .views import *

urlpatterns = [

    url(r'^index/$', list_index, name='index'),
    url(r'^(?P<id>\d+)/$', listdetail, name='detail'),
    url(r'^create/$', list_create, name='create'),
    url(r'^(?P<id>\d+)/delete/$', list_delete, name='delete'),
    url(r'^istatistik/$', istatistik, name='istatistik'),
    path('user_details/<str:type>', get_statistic_by_user, name='user_details'),
    path('statistic_charts', statistic_charts, name='statistic_charts')
]
