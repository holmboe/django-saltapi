# -*- coding: utf-8 -*-

# Import our libs
from .control import (
    wildcardtarget,
    get_salt_client,
    get_api_client,
    )
from .forms import ArgumentsForm

# Import Python libs
import json

# Import Django libs
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse


def JsonResponse(what):
    return HttpResponse(json.dumps(what), content_type='application/json')

# Externally accessible functions

#@login_required
@wildcardtarget
def ping(request, tgt):
    client = get_salt_client()
    ret = client.cmd(tgt, 'test.ping', ret='json')
    return JsonResponse(ret)

#@login_required
@wildcardtarget
def echo(request, tgt, arg):
    client = get_salt_client()
    ret = client.cmd(tgt, 'test.echo', arg, ret='json')
    return JsonResponse(ret)

#@login_required
@csrf_exempt
def apiwrapper(request):
    if request.method == 'POST':
        form = ArgumentsForm(request.POST)
    else:
        return render(request, 'index.html')

    if form.is_valid():
        client = get_api_client()
        lowdata = {
            'client': form.cleaned_data['client'],
            'tgt': form.cleaned_data['tgt'],
            'fun': form.cleaned_data['fun'],
            'arg': form.cleaned_data['arg'],
            }
        ret = client.run(lowdata)

        return JsonResponse(ret)
