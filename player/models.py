import feedparser
from urllib2 import urlopen
from hashlib import md5
from datetime import datetime
from time import strptime, mktime
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
    url = models.CharField(max_length = 256, unique=True)
    link = models.CharField(max_length = 256)
    description = models.TextField(max_length = 1024)
    title = models.CharField(max_length = 64, null=True, blank=True)
    pubdate = models.DateTimeField('Date of publication',null=True, blank=True)
    
    _raw_feed = "";
    # ??
    silent = models.BooleanField(default = True)
    
    def _get_feed(self):
        try:
            if not self._raw_feed:
                self._raw_feed = open("feeds/%s" % md5(self.url).hexdigest(), 'r').read()
        except:
            fd = open("feeds/%s" % md5(self.url).hexdigest(), 'w')
            self._raw_feed = urlopen(self.url).read()
            fd.write(self._raw_feed)
            fd.close()
            
    def _get_description(self):
        fparser = feedparser.parse(self._raw_feed)
        return fparser.feed.description

    def _get_title(self):
        fparser = feedparser.parse(self._raw_feed)
        return fparser.feed.title

    def _get_link(self):
        fparser = feedparser.parse(self._raw_feed)
        return fparser.feed.link

    def _get_pubdate(self):
        fparser = feedparser.parse(self._raw_feed)
        try:
            return fparser.feed.updated
        except:
            return fparser.entries[0].updated
    
    def _save_description(self):
        self.description = self._get_description()
        self.save()

    def _save_link(self):
        self.link = self._get_link()
        self.save()

    def _save_title(self):
        self.title = self._get_title()
        self.save()
    
    def _save_pubdate(self):
        self.pubdate = self._rfc2datetime
        self.save()
     
    def _rfc2datetime(self):
        time_struct = strptime(self._get_pubdate().split('-')[0].strip(), "%a, %d %b %Y %H:%M:%S")
        return datetime.fromtimestamp(mktime(time_struct))
        

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
