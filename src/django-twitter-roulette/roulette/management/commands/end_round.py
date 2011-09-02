from django.core.management.base import BaseCommand, CommandError
from roulette.models import *
from django.db.models import Sum
from random import choice
from django.conf import settings

import urlparse
import tweepy

class Command(BaseCommand):
    args = ''
    help = 'Ends a round, sends a tweet, starts a new round.'

    def handle(self, *args, **options):
        this_round = Round.objects.filter(round_end__gte=datetime.datetime.now()).order_by('round_end')[0]
        
        if this_round.bullet_set.count() > 10:
            top_ten = list(this_round.bullet_set.annotate(total=Sum('vote__value')).order_by('-total')[:10])
        else:
            top_ten = list(this_round.bullet_set.annotate(total=Sum('vote__value')).order_by('-total')[:this_round.bullet_set.count()])
        
        magazine = []
        for counter, bullet in enumerate(top_ten[::-1]):
            for i in range(counter):
                magazine.append(bullet)
        
        bullet_of_destiny = choice(magazine)
        print('bullet of destiny: %s' % bullet_of_destiny.tweet)
        
        victim = User.objects.filter(social_auth__provider__contains='twitter').order_by('?')[0]
        
        auth = tweepy.auth.OAuthHandler(settings.TWITTER_CONSUMER_KEY, settings.TWITTER_CONSUMER_SECRET)
        access_token = urlparse.parse_qs(victim.social_auth.filter(provider='twitter')[0].extra_data['access_token'])        
        
        auth.set_access_token(access_token['oauth_token'][0], access_token['oauth_token_secret'][0])
        api = tweepy.API(auth)
        api.update_status(bullet_of_destiny.tweet)