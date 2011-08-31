from django.utils import simplejson
from dajaxice.decorators import dajaxice_register
import datetime

@dajaxice_register
def submit_bullet(request, bullet):
    if not request.user.is_authenticated():
        return simplejson.dumps({'error':'Please log in first.'})
    else:
        if Bullet.objects.filter(tweet__iexact=bullet).count() > 0:
            return simplejson.dumps({'error':"It's been done before, try again"})
        else:
            this_round = Round.objects.filter(round_end__gte=datetime.datetime.now())[0]
            Bullet.objects.create(tweet=bullet, roulette_round=this_round, user=request.user)
            return simplejson.dumps({'message':'Your bullet has been submitted.'})