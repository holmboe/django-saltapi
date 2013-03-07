# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns('django_saltapi.views',
    url(r'^$', 'apiwrapper'),
    url(r'^ping/(?P<tgt>\w+)/$', 'ping'),
    url(r'^echo/(?P<tgt>\w+)/(?P<arg>\w+)/$', 'echo'),
)
