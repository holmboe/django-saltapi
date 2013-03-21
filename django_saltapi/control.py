# -*- coding: utf-8 -*-

# Import Django libs
from django.conf import settings

# Import Salt libs
import salt.config
import salt.client
import saltapi

def wildcardtarget(fun):
    '''
    Decorator to allow passing 'all' to the `tgt` argument, and it
    will translate into a '*' target which is then passed to Salt.
    '''
    def _wildcardtarget(*args, **kwargs):
        if kwargs.get('tgt', '') == 'all':
            kwargs['tgt'] = '*'
        return fun(*args, **kwargs)
    return _wildcardtarget

def get_salt_client():
    client = salt.client.LocalClient(
        c_path=settings.SALT_CONFIG['master_config']
        )
    return client

def get_api_client():
    opts = salt.config.client_config(
        settings.SALT_CONFIG['master_config']
        )
    opts.update(output='quiet')
    client = saltapi.APIClient(opts=opts)
    return client
