from django.contrib import admin
from django.conf.urls import include, url
import django.contrib.staticfiles
#import settings
from django.views.generic import ListView
from player.models import *

admin.autodiscover()
urlpatterns = [
    # Example:
    #(r'^podbox/', include('podbox.foo.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^feeds/$', ListView.as_view(model=Feed)),
    url(r'^updatefeed/(?P<feed_id>.*)$', 'player.views.update_feed'),
    url(r'^feed_ws/$', 'player.views.feed_ws'),
    url(r'^episodes_tl_ws/$', 'player.views.episodes_time_line'),
    url(r'^episodes_playlist/$', 'player.views.episodes_playlist'),
    url(r'^$', 'player.views.index'),
]
"""
if settings.DEBUG or settings.DATABASE_NAME.startswith("test_"):
    import os

    urlpatterns += patterns('',
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': os.path.join(settings.SITE_ROOT, 'static'), }),)
"""
