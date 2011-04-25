from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from player.models import *

def index(request):
    return render_to_response('player.html', locals())