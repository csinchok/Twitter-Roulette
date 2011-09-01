from django.template import Context, RequestContext, loader
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, Http404
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from models import *
from django.contrib.auth import logout

def logout_view(request, template_name='roulette/logout.html'):
    logout(request)
    this_round = Round.objects.filter(round_end__gte=datetime.datetime.now())[0]
    return render_to_response(template_name, {'this_round': this_round}, context_instance=RequestContext(request))

def home(request, template_name='roulette/home.html'):
    this_round = Round.objects.filter(round_end__gte=datetime.datetime.now())[0]
    bullets = Bullet.objects.filter(roulette_round=this_round).order_by("-date_submitted")[:10]
    for bullet in bullets:
        votes = Vote.objects.filter(bullet=bullet, user=request.user)
        if votes.count() == 1:
            if votes[0].value == 1:
                setattr(bullet, 'voted', 'up')
            else:
                setattr(bullet, 'voted', 'down')
        else:
            setattr(bullet, 'voted', 'undef')
    return render_to_response(template_name, {'ishome': True, 'bullets': bullets, 'this_round': this_round}, context_instance=RequestContext(request))
    
def login_error_view(request,template_name='roulette/login-error.html'):
	this_round = Round.objects.filter(round_end__gte=datetime.datetime.now())[0]
	return render_to_response(template_name, {'this_round': this_round}, context_instance=RequestContext(request))