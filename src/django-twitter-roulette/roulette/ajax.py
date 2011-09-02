from django.utils import simplejson
from dajaxice.decorators import dajaxice_register
import datetime
from models import *
from django.core import serializers

@dajaxice_register
def getfucked_latest_from(request,from_id=None):
    try:
        if not request.user.is_authenticated():
            return simplejson.dumps({'error': 'Please log in first.'})
        else:
			this_round = Round.objects.filter(round_end__gte=datetime.datetime.now())[0]
			if from_id == None: 
				from_id=0
			bullets = Bullet.objects.filter(roulette_round=this_round).filter(id__gt=from_id).order_by("-date_submitted")[:10]
			data = serializers.serialize("json", bullets)
			return data
    except Exception as e:
    	print(e)
    	return simplejson.dumps({'error': e.message})

@dajaxice_register
def submit_bullet(request, bullet):
    if not request.user.is_authenticated():
        return simplejson.dumps({'error': 'Please log in first.'})
    else:
        if Bullet.objects.filter(tweet__iexact=bullet).count() > 0:
            return simplejson.dumps({'error': "It's been done before, try again"})
        elif len(bullet) == 0:
            return simplejson.dumps({'error': "Maybe try actually typing something first"})
        elif len(bullet) > 140:
            return simplejson.dumps({'error': "Keep it to 140 characters, bro"})
        else:
            this_round = Round.objects.filter(round_end__gte=datetime.datetime.now())[0]
            Bullet.objects.create(tweet=bullet, roulette_round=this_round, user=request.user)
            return simplejson.dumps({'message': 'Your bullet has been submitted'})

@dajaxice_register        
def vote(request, bullet_id, value):
    if not request.user.is_authenticated():
        return simplejson.dumps({'error': 'Please log in first.'})
    else:
        try:
            bullet = Bullet.objects.get(id=bullet_id)
        except:
            return simplejson.dumps({'error': 'No such bullet.'})
        votes = Vote.objects.filter(bullet=bullet, user=request.user)
        if votes.count() > 0:
            vote = votes[0]
            vote.value = value
            vote.save()
        else:
            vote = Vote.objects.create(user=request.user, bullet=bullet, value=value)
        return simplejson.dumps({'message': 'Thanks for voting', 'bullet_id': bullet_id, 'value': value, 'total': bullet.score()})