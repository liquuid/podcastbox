# -*- coding: utf-8 -*-
import json
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from player.models import *
from django.http import HttpResponse

def index(request):
    episodes = Episode.objects.all().order_by('-updated')[:50]
    return render_to_response('index.html', locals())

def feed_ws(request, user_id):
    feeds = '{'
    for feed in UserProfile.objects.get(user_id=user_id).feeds.values():
        #import pdb; pdb.set_trace()
        feeds += " '%s':{ 'url':'%s', 'silent':'%s', 'title':'%s'  }," % ( feed['id'], feed['url'], feed['silent'], feed['title'] )
    feeds += '}'
    return HttpResponse(json.dumps(eval(feeds)))

def episodes_time_line(request, user_id):
    episodes = '{'
    episode_list = Episode.objects.none() 
    for feed in UserProfile.objects.get(user_id=user_id).feeds.all():
        episode_list = Episode.objects.filter(feeds=feed) | episode_list
    
    for episode in episode_list.order_by('-updated').values():
        episodes += " '%s':{ 'url':'%s', 'updated':'%s','summary':'%s'  , 'title':'%s' , 'feed':'%s' }," % ( episode['id'], episode['url'], episode['updated'], episode['summary'], episode['title'],  episode['feeds_id'])
        print episode

    #print episode_list.order_by('-updated')
    episodes += '}'
    return HttpResponse(json.dumps(eval(episodes)))


def update_feed(request, feed_id):
    feed = Feed.objects.get(id=feed_id)
    feed.update_episodes()
    return HttpResponse("feito") 

