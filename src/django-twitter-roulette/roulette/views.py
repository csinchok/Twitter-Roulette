from django.template import Context, RequestContext, loader
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, Http404
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from models import *

def home(request, template_name='roulette/home.html'):
    return render_to_response(template_name, {}, context_instance=RequestContext(request))