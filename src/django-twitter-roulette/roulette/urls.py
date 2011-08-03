from django.conf.urls.defaults import *

urlpatterns = patterns('',
    
    (r'^$', 'roulette.views.home'),
)