from coffin.shortcuts import render_to_response
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import logout as _logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseServerError
from django.shortcuts import redirect
from django.template import RequestContext

import cjson

from metakv import models

def r2r(template, request, data=None):
    data = data or {}
    return render_to_response(template, data, context_instance=RequestContext(request))

def json_response(func):
    def decorated(*args, **kwargs):
        return HttpResponse(cjson.encode(func(*args, **kwargs)), mimetype="application/json")
    return decorated

def logout(request):
    _logout(request)
    return redirect('index')

def index(request):
    return r2r("index.jinja", request)

