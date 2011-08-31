from django.conf.urls.defaults import *

urlpatterns = patterns('',
    
    (r'^$', 'roulette.views.home'),
    (r'^logout$', 'roulette.views.logout_view'),
)