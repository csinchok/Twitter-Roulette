from twitterroulette.settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'csinchok_social_roulette',                      # Or path to database file if using sqlite3.
        'USER': 'csinchok_social_roulette',                      # Not used with sqlite3.
        'PASSWORD': PROD_PASSWORD,                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

ADMIN_MEDIA_PREFIX = '/admin_media/'

DEBUG = True
TEMPLATE_DEBUG = DEBUG
DAJAXICE_DEBUG = DEBUG