# -*- coding: utf-8 -*-
import json
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from player.models import *
from django.http import HttpResponse

def index(request):
    return render_to_response('player.html', locals())

def feed_ws(request, user_id):
    feeds = '{'
    for feed in UserProfile.objects.get(id=user_id).feeds.values():
        feeds += " '%s':{ 'url':'%s', 'silent':'%s', 'name':'%s'  }," % ( feed['id'], feed['url'], feed['silent'], feed['name'] )
    feeds += '}'
    return HttpResponse(json.dumps(eval(feeds)))
