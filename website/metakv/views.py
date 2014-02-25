from coffin.shortcuts import render_to_response
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import logout as _logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponse, HttpResponseForbidden, HttpResponseServerError
from django.shortcuts import redirect
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from social_auth.models import UserSocialAuth

import base64
import cjson
import requests

from metakv import models

def r2r(template, request, data=None):
    data = data or {}
    return render_to_response(template, data, context_instance=RequestContext(request))

def json_response(func):
    def decorated(*args, **kwargs):
        return HttpResponse(cjson.encode(func(*args, **kwargs)), mimetype='application/json')
    return decorated

def logout(request):
    _logout(request)
    return redirect('index')

def index(request):
    if request.user.is_authenticated():
        access_token = request.user.social_auth.get().tokens['access_token']
    return r2r("index.jinja", request, locals())

@csrf_exempt
@require_POST
def api_set(request, key):
    access_token = request.GET.get('access_token')
    key = base64.b32encode(key)
    value = base64.b32encode(request.body)

    github_payload = {'labels': ['meta'], 'title': key, 'body': value}
    headers = {'Authorization': 'token {}'.format(access_token)}
    response = requests.post(
            'https://api.github.com/repos/mrooney/metakv/issues',
            data=cjson.encode(github_payload),
            headers=headers
    )
    return HttpResponse(unicode(response))

def api_get(request, key):
    access_token = request.GET.get('access_token')
    key = base64.b32encode(key)
    for usa in UserSocialAuth.objects.all():
        if usa.tokens['access_token'] == access_token:
            author = usa.user.username
            break
    else:
        raise Http404

    url = 'https://api.github.com/search/issues?q={}+label:meta+author:{}+in:title&sort=created&order=desc'.format(key, author)
    response = requests.get(url)
    if response.status_code == 200:
        value = base64.b32decode(cjson.decode(response.text)['items'][0]['body'])
        return HttpResponse(value)
    else:
        return HttpResponse(unicode(response))

