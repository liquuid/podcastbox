from django.conf.urls.defaults import *
from django.contrib import admin
#from django.conf.urls.static import static
import django.contrib.staticfiles
import settings
from django.views.generic import ListView
from player.models import *


admin.autodiscover()
urlpatterns = patterns('',
    # Example:
    #(r'^podbox/', include('podbox.foo.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^feeds/$', ListView.as_view(model=Feed)),
    (r'^feed_ws/(?P<user_id>.*)$', 'podbox.player.views.feed_ws'),
    (r'^$', 'podbox.player.views.index'),
)
"""
if settings.DEBUG or settings.DATABASE_NAME.startswith("test_"):
    import os

    urlpatterns += patterns('',
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': os.path.join(settings.SITE_ROOT, 'static'), }),)
"""
