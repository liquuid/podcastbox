from django.contrib import admin

from podbox.player.models import *

admin.site.register(UserProfile)
admin.site.register(Feed)
admin.site.register(Episode)