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
    feeds = '{'
    for feed in UserProfile.objects.get(user_id=request.user.id).feeds.values():
        # import pdb; pdb.set_trace()
        feeds += " '%s':{ 'id':'%s', 'url':'%s', 'title':'%s'  }," % (
        feed['id'], feed['id'], feed['url'], feed['title'])
    feeds += '}'
    return HttpResponse(json.dumps(eval(feeds)))


def user_feed_ws(request):
    feeds = '{'
    for feed in UserProfile.objects.get(user_id=request.user.id).feeds.values():
        # import pdb; pdb.set_trace()
        feeds += " '%s':{ 'id':'%s', 'url':'%s', 'silent':'%s', 'title':'%s'  }," % (
        feed['id'], feed['id'], feed['url'], feed['silent'], feed['title'])
    feeds += '}'
    return HttpResponse(json.dumps(eval(feeds)))


def episodes_time_line(request):
    # episodes = '{'
    episodes = '{'
    episode_list = Episode.objects.none()
    for feed in UserProfile.objects.get(user_id=request.user.id).feeds.all():
        episode_list = Episode.objects.filter(feeds=feed) | episode_list

    for episode in episode_list.order_by('-updated').values():
        episodes += " '%s':{'id':'%s', 'url':'%s', 'updated':'%s','summary':'%s'  , 'title':'%s' , 'feed_id':'%s' }," % (
        episode['id'], episode['id'], episode['url'], episode['updated'], episode['summary'], episode['title'],
        episode['feeds_id'])
        print(episode['id'])

    # print episode_list.order_by('-updated')
    episodes += '}'
    return HttpResponse(json.dumps(eval(episodes)))


def episodes_playlist(request):
    episodes = []
    episode_list = Episode.objects.none()
    for feed in UserProfile.objects.get(user_id=request.user.id).feeds.all():
        episode_list = Episode.objects.filter(feeds=feed) | episode_list

    for episode in episode_list.order_by('-updated').values():
        episodes.append(episode['id'])

    return HttpResponse(json.dumps(episodes))


def user_episodes_time_line(request):
    episodes = '{'
    episode_list = Episode.objects.none()
    for feed in UserProfile.objects.get(user_id=request.user.id).feeds.all():
        episode_list = Episode.objects.filter(feeds=feed) | episode_list

    for episode in episode_list.order_by('-updated').values():
        episodes += " '%s':{'id':'%s', 'url':'%s', 'updated':'%s','summary':'%s'  , 'title':'%s' , 'feed_id':'%s' }," % (
        episode['id'], episode['id'], episode['url'], episode['updated'], episode['summary'], episode['title'],
        episode['feeds_id'])
        print(episode)

    # print episode_list.order_by('-updated')
    episodes += '}'
    return HttpResponse(json.dumps(eval(episodes)))


def update_feed(request, feed_id):
    feed = Feed.objects.get(id=feed_id)
    feed.update_episodes()
    return HttpResponse("feito")

