from django.urls import path
from django.contrib import admin

from .views import (
	post_list,
	post_create,
	post_detail,
	post_update,
	post_delete,
	)

urlpatterns = [
	path('', post_list, name='list'),
    path('create/$', post_create),
    path('(?P<slug>[\w-]+)/$', post_detail, name='detail'),
    path('(?P<slug>[\w-]+)/edit/$', post_update, name='update'),
    path('(?P<slug>[\w-]+)/delete/$', post_delete),
    #url(r'^posts/$', "<appname>.views.<function_name>"),
]
