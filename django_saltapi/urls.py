# -*- coding: utf-8 -*-

from django_saltapi.utils import REGEX_JID, REGEX_HOSTNAME

from django.conf.urls import patterns, url

urlpatterns = patterns('django_saltapi.views',
    url(r'^$', 'apiwrapper'),

    url(r'^minions/$', 'minions_list'),
    url(r'^minions/(?P<tgt>' + REGEX_HOSTNAME + ')/$', 'minions_details'),

    url(r'^jobs/$', 'jobs_list'),
    url(r'^jobs/(?P<jid>' + REGEX_JID + ')/$', 'jobs_details'),

    url(r'^ping/(?P<tgt>' + REGEX_HOSTNAME + ')/$', 'ping'),
    url(r'^echo/(?P<tgt>' + REGEX_HOSTNAME + ')/(?P<arg>\w+)/$', 'echo'),
)
