from coffin.conf.urls import *
from django.conf import settings
from django.contrib import admin
from django.core.urlresolvers import reverse_lazy

admin.autodiscover()

app_urls = (
    url(r'^%s/'%name, 'metakv.views.%s'%name, name=name) for name in [
        'logout',
    ]
)

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('social_auth.urls')),
    url(r'^$', 'metakv.views.index', name='index'),
    url(r'^set/(.*)$', 'metakv.views.api_set', name='set'),
    url(r'^get/(.*)$', 'metakv.views.api_get', name='get'),
    *app_urls
)
