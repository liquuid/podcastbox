# -*- coding: utf-8 -*-
from datetime import datetime
from hashlib import md5
from time import strptime, mktime
from urllib.request import urlopen

import feedparser
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save


class UserProfile(models.Model):
    user = models.ForeignKey('auth.User')
    feeds = models.ManyToManyField('Feed', null=True, blank=True)

    def __str__(self):
        return "%s's profile" % self.user


# codigo magico
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile, created = UserProfile.objects.get_or_create(user=instance)


post_save.connect(create_user_profile, sender=User)


class UserEpisode(models.Model):
    episode = models.ForeignKey('Episode')
    is_new = models.BooleanField(default=True)
    favorite = models.BooleanField(default=False)


class UserFeed(models.Model):
    episode = models.ForeignKey('Feed')
    favorite = models.BooleanField(default=False)
    silent = models.BooleanField(default=False)


class Episode(models.Model):
    title = models.CharField(max_length=64)
    url = models.CharField(max_length=256)
    updated = models.DateTimeField()
    summary = models.TextField(max_length=512, null=True, blank=True)
    feeds = models.ForeignKey('Feed')

    def _parse_data(self, data):
        self.title = data['title']
        self.url = data["links"][1]["href"]
        self.updated = datetime.strptime(data['updated'][:25].strip(), "%a, %d %b %Y %H:%M:%S")
        self.summary = data['summary']

    def __str__(self):
        return "%s" % (self.title)


class Category(models.Model):
    """
    >>> c = Category()
    >>> c.name = "name"
    >>> print(c.name)
    name
    """
    name = models.CharField(max_length=256, unique=True, null=False, blank=False)

    def __str__(self):
        return "%s" % (self.name)


class Feed(models.Model):
    url = models.CharField(max_length=256, unique=True)
    link = models.CharField(max_length=256, null=True, blank=True)
    description = models.TextField(max_length=1024, null=True, blank=True)
    title = models.CharField(max_length=64, null=True, blank=True)
    pubdate = models.DateTimeField('Date of publication', null=True, blank=True)
    category = models.ForeignKey('Category')

    _raw_feed = "";

    def update_episodes(self):
        self._get_feed()
        self._create_episodes()

    def _get_feed(self):
        try:
            if not self._raw_feed:
                self._raw_feed = open("feeds/%s" % md5(self.url.encode("utf-8")).hexdigest(), 'r',
                                      encoding='utf-8').read()
        except:
            fd = open('feeds/%s' % md5(self.url.encode("utf-8")).hexdigest(), 'w')
            self._raw_feed = urlopen(self.url).read()
            fd.write(str(self._raw_feed))
            fd.close()

    def _get_description(self):
        fparser = feedparser.parse(self._raw_feed)
        return fparser.feed.description

    def _list_episodes(self):
        # TODO: teste
        fparser = feedparser.parse(self._raw_feed)
        return fparser.entries

    def _create_episode(self, episode_data):
        # TODO: teste
        episode = Episode()
        episode._parse_data(episode_data)
        try:
            Episode.objects.get(url=episode.url)
            print("ja existe")
        except:
            episode.feeds = self
            episode.save()

    def _create_episodes(self):
        # TODO: teste
        for episode_data in self._list_episodes():
            self._create_episode(episode_data)

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
        self.pubdate = self._rfc2datetime()
        self.save()

    def _rfc2datetime(self):
        time_struct = strptime(self._get_pubdate()[:25], "%a, %d %b %Y %H:%M:%S")
        return datetime.fromtimestamp(mktime(time_struct))

    def __str__(self):
        if self.title:
            return self.title
        else:
            return self.url
