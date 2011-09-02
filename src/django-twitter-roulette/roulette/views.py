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
    return render_to_response(template_name, {'ishome': True, 'this_round': this_round}, context_instance=RequestContext(request))
    
def login_error_view(request,template_name='roulette/login-error.html'):
	this_round = Round.objects.filter(round_end__gte=datetime.datetime.now())[0]
	return render_to_response(template_name, {'this_round': this_round}, context_instance=RequestContext(request))