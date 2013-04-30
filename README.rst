===============
Django Salt API
===============

This Django app serves as a REST API for Salt. It is basically a very
thing wrapper around the salt-api_ package.

.. _salt-api: https://github.com/saltstack/salt-api

Status
------

The main motivation behind creating a Django package to interface with
Salt is that Django is already in our software stack. Since then
salt-api has become more flexible in the ways it can be deployed -- it
is now possible to deploy its `rest_cherrypy`_ module on any compliant
WSGI server (in contrast to running `salt-api` in a separate process).
In addition to that there is an even slimmer alternative, though with
less features, in the `rest_wsgi`_ module. I encourage you to have a
look at them before deciding to use django-saltapi.

.. _rest_cheerypy: http://salt-api.readthedocs.org/en/latest/ref/netapis/all/saltapi.netapi.rest_cherrypy.html
.. _rest_wsgi: http://salt-api.readthedocs.org/en/latest/ref/netapis/all/saltapi.netapi.rest_wsgi.html

Since salt-api has solved most of the motivations behind the inception
of django-saltapi it is likely that this packages raison d'etre will
be to utilize more of the functionality in the Django REST Framework.
Future developments will likely be towards this goal.

This package comes with some caveats. This app compared to salt-api:

 - this app only supports x-www-form-urlencoded data input for the API
   wrapper or input snarfed from the URL, whereas salt-api supports
   other data formats

 - this app supports only JSON data output

.. note:: Currently the API does not require authentication and two
          API functions are exposed without CSRF protection, though
          they are harmless from an integrity perspective. See
          `views.py` to enable authentication.


Installation
------------

1. Add `django_saltapi` to your `INSTALLED_APPS` setting in your
   project `settings.py`::

      INSTALLED_APPS = (
          [...]
          'django_saltapi',
      )

2. Add Salt settings in your project `settings.py`::

      SALT_CONFIG = {
          'master_config': '/etc/salt/master',
      }

2. Include the package URLconf in your project `urls.py` like so::

      url(r'^api/salt/', include('django_saltapi.urls')),


Usage
-----

.. note:: The documentation and some scripts refer to the host as
          "salt" where the API is running, YMMV.

1. Visit http://salt/api/salt/ to view the default static HTML page.

2. Issue a Salt ping to all minions via the Salt API wrapper::

      django-saltapi '*' test.ping

3. Try out the explicitly exposed REST API functions (see views.py)::

      django-saltapi-ping all
      django-saltapi-echo all x
      django-saltapi-job
      django-saltapi-job <jid>
      django-saltapi-minion
      django-saltapi-minion <mid>
