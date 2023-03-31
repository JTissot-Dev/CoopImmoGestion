import pytest
from flask import session
from coopimmogestion import create_app
from coopimmogestion.config.TestingConfig import TestingConfig
from coopimmogestion.models.Address import Address
from coopimmogestion.models.AppUser import AppUser
from coopimmogestion.db.db import db
from datetime import datetime as dt
from coopimmogestion.crypt.crypt import bcrypt


@pytest.fixture()
def app():
    app = create_app(TestingConfig)
    with app.app_context():
        db.create_all()
        create_user_test(app)

    yield app

    with app.app_context():
        db.drop_all()


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()


def create_user_test(app):
    with app.app_context():
        address_test: Address = Address(None, 'test', 1, 'C', '00000', 'Bron')
        db.session.add(address_test)
        db.session.commit()
        user_test_password = bcrypt.generate_password_hash('Test1*').decode('utf-8')
        user_test: AppUser = AppUser(None, 'test', 'test', dt.now(), '0000000000',
                                     'test@test.fr', address_test, 'user', user_test_password)
        db.session.add(user_test)
        db.session.commit()


