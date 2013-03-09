# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns('django_saltapi.views',
    url(r'^$', 'apiwrapper'),

    url(r'^minions/$', 'minions', {'mid': None}),
    url(r'^minions/(?P<mid>\w+)/$', 'minions'),

    url(r'^jobs/$', 'jobs', {'jid': None}),
    url(r'^jobs/(?P<jid>\d+)/$', 'jobs'),

    url(r'^ping/(?P<tgt>\w+)/$', 'ping'),
    url(r'^echo/(?P<tgt>\w+)/(?P<arg>\w+)/$', 'echo'),
)
