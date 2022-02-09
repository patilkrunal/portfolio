import dj_database_url
import django_on_heroku
from dotenv import load_dotenv
import os
from pathlib import Path
from .base import *


DEBUG = False
print("DEBUG", DEBUG)

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'patilkrunal.herokuapp.com', '*']

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    "default": dj_database_url.config(default=os.getenv("DATABASE_URL"))
}

CORS_ORIGIN_ALLOW_ALL = True

CORS_ORIGIN_WHITELIST = (
    'http://localhost:3000',
    'https://kp.gtsb.io',
    'https://kpstaging.gatsbyjs.io',
    'https://patilkrunal.me',
    'https://patilkrunal.vercel.app',
)


TEST_RUNNER = 'django_on_heroku.HerokuDiscoverRunner'
django_on_heroku.settings(locals())