import django_on_heroku
from decouple import config
from .base import *

#SECRET_KEY = 'django-insecure-&7mv!q56zhkpy*ku8*dt8l32zq=!z@u+nus+1!#6qc)n06a7$g'
#DEBUG = True
#ALLOWED_HOSTS = []

SECRET_KEY = config('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = [
  'ryowu-base-blog.herokuapp.com',
  'ryowu.blog'
]
