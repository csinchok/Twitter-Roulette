from django.core.management.base import BaseCommand, CommandError
from roulette.models import *
from django.db.models import Sum
from random import choice

import csv

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