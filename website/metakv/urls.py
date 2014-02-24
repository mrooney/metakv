from coffin.conf.urls import *
from django.conf import settings
from django.contrib import admin
from django.core.urlresolvers import reverse_lazy

admin.autodiscover()

app_urls = (
    url(r'^%s/'%name, 'metakv.views.%s'%name, name=name) for name in [
    ]
)

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'metakv.views.index', name='index'),
    *app_urls
)
