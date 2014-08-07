from django.conf.urls import patterns, include, url
from apps.home.views import index
from django.contrib import admin
from apps.demo.views import hello
from apps.demo.views import current_datetime
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ApiCloud.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    (r'^$', index),
    url(r'^index/$', index),
    url(r'^admin/', include(admin.site.urls)),

    #demo
    (r'^hello/$', hello),
    (r'^current_datetime/$', current_datetime),
)

