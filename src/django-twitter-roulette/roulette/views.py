from django.template import Context, RequestContext, loader
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, Http404
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from models import *