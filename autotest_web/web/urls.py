# -*- coding:utf-8 -*-
# @Time    : 2020/5/21 15:17
# @Author  : zengln
# @File    : urls.py

from django.urls import path, re_path
from web import views

urlpatterns = [
    path('', views.index),
]