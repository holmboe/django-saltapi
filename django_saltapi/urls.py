# -*- coding: utf-8 -*-

from django_saltapi.utils import REGEX_JID, REGEX_HOSTNAME

from django.conf.urls import patterns, url

urlpatterns = patterns('django_saltapi.views',
    url(r'^$', 'apiwrapper'),

    url(r'^minions/$', 'minions', {'mid': None}),
    url(r'^minions/(?P<mid>' + REGEX_HOSTNAME + ')/$', 'minions'),

    url(r'^jobs/$', 'jobs', {'jid': None}),
    url(r'^jobs/(?P<jid>' + REGEX_JID + ')/$', 'jobs'),

    url(r'^ping/(?P<tgt>' + REGEX_HOSTNAME + ')/$', 'ping'),
    url(r'^echo/(?P<tgt>' + REGEX_HOSTNAME + ')/(?P<arg>\w+)/$', 'echo'),
)
