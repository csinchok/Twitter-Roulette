from __future__ import with_statement
from fabric.api import *
from fabric.contrib.console import confirm

env.hosts = ['csinchok.webfactional.com']
env.user = 'csinchok'

webapp_path = '/home/csinchok/webapps/social_roulette'

def test():
    local('./bin/test', capture=False)

def pack():
    local('git archive --format zip master --output=social_roulette.zip', capture=False)

def prepare_deploy():
    pack()

def deploy_prod_code():
    prepare_deploy()
    
    put('social_roulette.zip', '/home/csinchok/')
    run('unzip -o /home/csinchok/social_roulette.zip -d %s' % webapp_path)
    put('twitterroulette/social_keys.py', '/home/csinchok/webapps/social_roulette/twitterroulette/social_keys.py')
    
    with cd(webapp_path):
        run('touch bin/django.wsgi')
        run('apache2/bin/restart')
    
    run('rm /home/csinchok/social_roulette.zip')

def deploy_prod():
    prepare_deploy()
    
    put('./social_roulette.zip', '/home/csinchok/')
    run('unzip -o /home/csinchok/social_roulette.zip -d %s' % webapp_path)
    put('twitterroulette/social_keys.py', '/home/csinchok/webapps/social_roulette/twitterroulette/social_keys.py')
    
    with cd(webapp_path):
        run('python2.6 ./bootstrap.py')
        run('bin/buildout -c production.cfg')
        run('bin/django syncdb --noinput')
        run('bin/django migrate')
        run('touch bin/django.wsgi')
        run('apache2/bin/restart')
    
    run('rm /home/csinchok/social_roulette.zip')