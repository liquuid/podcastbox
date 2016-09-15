# Register your models here.
# -*- coding: utf-8 -*-

from django.contrib import admin

from podbox.core.models import *

admin.site.register(UserProfile)
admin.site.register(Feed)
admin.site.register(Episode)
admin.site.register(UserFeed)
admin.site.register(UserEpisode)
admin.site.register(Category)
