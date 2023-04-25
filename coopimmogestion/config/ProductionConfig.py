import os
from .Config import Config


class ProductionConfig(Config):
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    TESTING = False
    DEBUG = False
    SESSION_COOKIE_SECURE = True
    SCHEDULER_API_ENABLED = True
