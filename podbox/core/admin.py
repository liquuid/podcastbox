# Register your models here.
# -*- coding: utf-8 -*-

from django.contrib import admin

from podbox.core.models import UserProfile, Feed, Episode, UserFeed, UserEpisode, Category

admin.site.register(UserProfile)
admin.site.register(Feed)
admin.site.register(Episode)
admin.site.register(UserFeed)
admin.site.register(UserEpisode)
admin.site.register(Category)
