# -*- coding: utf-8 -*-
import json
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from podbox.core.models import *
from django.http import HttpResponse


def index(request):
    # episodes = Episode.objects.all().order_by('-updated')[:50]
    # import pdb; pdb.set_trace()
    feeds = UserProfile.objects.get(user_id=request.user.id).feeds.all()
    return render_to_response('index.html', locals())


def feed_ws(request):
    feeds = {}
    for feed in UserProfile.objects.get(user_id=request.user.id).feeds.values():
        feeds[feed['id']] = {'id': feed['id'],
                             'url': feed['url'],
                             'title': feed['title']}

    return HttpResponse(json.dumps(feeds))

def user_feed_ws(request):
    feeds = {}
    for feed in UserProfile.objects.get(user_id=request.user.id).feeds.values():
        feeds[feed['id']] = {'id': feed['id'],
                              'url': feed['url'],
                              'silent': feed['silent'],
                              'title': feed['title']}

    return HttpResponse(json.dumps(feeds))


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


def episodes_playlist(request):
    episode_list = Episode.objects.none()
    for feed in UserProfile.objects.get(user_id=request.user.id).feeds.all():
        episode_list = Episode.objects.filter(feeds=feed) | episode_list

    episodes = [episode['id'] for episode in episode_list.order_by('-updated').values()]

    return HttpResponse(json.dumps(episodes))


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

def update_feed(request, feed_id):
    feed = Feed.objects.get(id=feed_id)
    feed.update_episodes()
    return HttpResponse("feito")
