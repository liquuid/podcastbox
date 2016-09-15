# -*- coding: utf-8 -*-
import json

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from podbox.core.models import *


@login_required
def index(request):
    feeds = UserProfile.objects.get(user_id=request.user.id).feeds.all()
    return render(request, 'index.html')


@login_required
def feed_ws(request):
    feeds = {}
    for feed in UserProfile.objects.get(user_id=request.user.id).feeds.values():
        feeds[feed['id']] = {'id': feed['id'],
                             'url': feed['url'],
                             'title': feed['title']}

    return HttpResponse(json.dumps(feeds))


@login_required
def user_feed_ws(request):
    feeds = {}
    for feed in UserProfile.objects.get(user_id=request.user.id).feeds.values():
        feeds[feed['id']] = {'id': feed['id'],
                             'url': feed['url'],
                             'silent': feed['silent'],
                             'title': feed['title']}

    return HttpResponse(json.dumps(feeds))


@login_required
def episodes_time_line(request):
    episodes = {}
    episode_list = Episode.objects.none()
    for feed in UserProfile.objects.get(user_id=request.user.id).feeds.all():
        episode_list = Episode.objects.filter(feeds=feed) | episode_list

    for episode in episode_list.order_by('-updated').values():
        episodes[episode['id']] = {'id': episode['id'],
                                   'url': episode['url'],
                                   'updated': episode['updated'].strftime("%d/%m/%Y"),
                                   'summary': episode['summary'],
                                   'title': episode['title'],
                                   'feed_id': episode['feeds_id']
                                   }

    return HttpResponse(json.dumps(episodes))


@login_required
def episodes_playlist(request):
    episode_list = Episode.objects.none()
    for feed in UserProfile.objects.get(user_id=request.user.id).feeds.all():
        episode_list = Episode.objects.filter(feeds=feed) | episode_list

    episodes = [episode['id'] for episode in episode_list.order_by('-updated').values()]

    return HttpResponse(json.dumps(episodes))


@login_required
def user_episodes_time_line(request):
    episodes = {}
    episode_list = Episode.objects.none()
    for feed in UserProfile.objects.get(user_id=request.user.id).feeds.all():
        episode_list = Episode.objects.filter(feeds=feed) | episode_list

    for episode in episode_list.order_by('-updated').values():
        episodes[episode['id']] = {'id': episode['id'],
                                   'url': episode['url'],
                                   'updated': episode['updated'].strftime("%d/%m/%Y"),
                                   'summary': episode['summary'],
                                   'title': episode['title'],
                                   'feed_id': episode['feeds_id']
                                   }

    return HttpResponse(json.dumps(episodes))


@login_required
def update_feed(request, feed_id):
    feed = Feed.objects.get(id=feed_id)
    feed.update_episodes()
    return HttpResponse("feito")
