from .Config import Config


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:Development_2023@localhost:5432/coopimmogestiontest'
    

