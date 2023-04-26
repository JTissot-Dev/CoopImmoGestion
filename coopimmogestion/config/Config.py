import secrets
import os


class Config(object):
    SECRET_KEY = secrets.token_hex(16)
    TESTING = False
    SESSION_COOKIE_PATH = '/'
    # Schedule tasks config
    SCHEDULER_API_ENABLED = True
    # smtp config
    MAIL_SERVER ='smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USERNAME = 'coopimmogestion@gmail.com'
    MAIL_PASSWORD = os.environ.get('SMTP_PASSWORD')
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True





