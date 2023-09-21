from .base import *
import environ


DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']


env = environ.Env()
environ.Env.read_env(str(BASE_DIR/'.env'))

SECRET_KEY = env.str('SECRET_KEY')

DATABASES = {
    'default': {
        'ENGINE': env.str('DB_ENGINE'),
        'NAME': env.str('DB_NAME'),
        'USER': env.str('DB_USER'),
        'PASSWORD': env.str('DB_PASSWORD'),
        'HOST': env.str('DB_HOST'),
        'PORT': env.str('DB_PORT')
    }
}