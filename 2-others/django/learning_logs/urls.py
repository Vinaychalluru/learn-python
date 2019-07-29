from django.conf.urls import url
from django.urls import path

from . import views

# app_name = 'learning_logs'
urlpatterns = [
    path('', views.index, name='index'),
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
]