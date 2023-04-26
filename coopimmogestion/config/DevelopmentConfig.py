from .Config import Config


class DevelopmentConfig(Config):
    TESTING = False
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:Development_2023@localhost:5432/coopimmogestion"
    DEBUG = True
    TEMPLATES_AUTO_RELOAD = True



