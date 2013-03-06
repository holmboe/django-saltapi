# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns('django_saltapi.views',
    url(r'^$', 'apiwrapper'),
    url(r'^ping/(?P<tgt>[a-zA-Z0-9.-]+)/$', 'ping'),
    url(r'^echo/(?P<tgt>[a-zA-Z0-9.-]+)/(?P<arg>\w+)/$', 'echo'),
)
