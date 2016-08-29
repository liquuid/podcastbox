"""podbox URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from podbox.core import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^feeds/$', ListView.as_view(model=Feed)),
    url(r'^updatefeed/(?P<feed_id>.*)$', views.update_feed),
    url(r'^feed_ws/$', views.feed_ws),
    url(r'^episodes_tl_ws/$', views.episodes_time_line),
    url(r'^episodes_playlist/$', views.episodes_playlist),
    url(r'^$', views.index)

]
