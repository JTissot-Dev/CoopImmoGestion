import secrets


class Config(object):
    SECRET_KEY = secrets.token_hex(16)
    TESTING = False
    SESSION_COOKIE_PATH = '/'






