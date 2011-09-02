from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.db.models import Sum, Avg
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
import datetime
from roulette.utils import calculate_luck

class Round(models.Model):
    """A Round of Twitter Roulette"""
    
    minimum_players = models.IntegerField(default=25)
    round_end = models.DateTimeField(blank=True, default=(datetime.datetime.now() + datetime.timedelta(days=1)))
    
    class Meta:
        pass

    def __unicode__(self):
        return u"Round ending: %s" % self.round_end


class Bullet(models.Model):
    """(Bullet description)"""
    
    user = models.ForeignKey(User)
    tweet = models.CharField(max_length=140)
    roulette_round = models.ForeignKey(Round)
    date_submitted = models.DateTimeField(blank=True, default=datetime.datetime.now())
    
    class Meta:
        pass

    def score(self):
        total = self.vote_set.aggregate(total=Sum('value'))['total']
        if total is None:
            return 0
        else:
            return total

    def __unicode__(self):
        return u"%s : \"%s\"" % (self.user, self.tweet[:25])


class Vote(models.Model):
    
    user = models.ForeignKey(User)
    bullet = models.ForeignKey(Bullet)
    value = models.IntegerField(default=1)
    
    def __unicode__(self):
        return u"%s voted %s on %s" % (self.user, self.value, self.bullet)


class Player(User):

    class Meta:
        proxy = True

    @property
    def luck_of_the_draw(self):
        this_round = Round.objects.filter(round_end__gte=datetime.datetime.now())[0]
        try:
            total_votes = Vote.objects.filter(bullet__roulette_round=this_round).count()
            my_bullet_score = self.bullet_set.get(roulette_round=this_round)[0].score()
            avg_bullet_score = this_round.bullet_set.aggregate(Avg('vote'))['vote__avg']
            if (avg_bullet_score is None):
                avg_bullet_score = 0
            return calculate_luck(my_bullet_score, avg_bullet_score, total_votes)
        except ObjectDoesNotExist:
            return None

