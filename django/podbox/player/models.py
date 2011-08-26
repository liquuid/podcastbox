from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class UserProfile(models.Model):
    user = models.ForeignKey('auth.User')
    feeds = models.ManyToManyField('Feed', null=True, blank=True)

    def __str__(self):
        return "%s's profile" % self.user

#codigo magico
def create_user_profile(sender, instance, created, **kwargs):
    if created:
       profile, created = UserProfile.objects.get_or_create(user=instance)

post_save.connect(create_user_profile, sender=User)

class Feed(models.Model):
    url = models.CharField(max_length = 256)
    title = models.CharField(max_length =64, null=True, blank=True)
    # ??
    silent = models.BooleanField(default = True)
    
    def __str__(self):
        if self.title:
            return self.title
        else:
            return self.url

class Episode(models.Model):
    title = models.CharField(max_length = 64)
    url = models.CharField(max_length = 256)
    feeds = models.ForeignKey('Feed')

    def __str__(self):
        return "%s of %s" % (self.name, self.podcast.name)
