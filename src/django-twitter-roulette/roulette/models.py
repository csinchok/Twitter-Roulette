from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
import datetime

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
    
    class Meta:
        pass

    def __unicode__(self):
        return u"%s : \"%s\"" % (self.user, self.tweet[:25])


class Vote(models.Model):
    
    user = models.ForeignKey(User)
    bullet = models.ForeignKey(Bullet)
    value = models.BooleanField(default=True)
    
    def __unicode__(self):
        return u"%s voted %s on %s" % (self.user, self.value, self.bullet)