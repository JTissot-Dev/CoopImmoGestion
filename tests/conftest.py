import pytest
from  coopimmogestion import create_app
from  coopimmogestion.config.TestingConfig import TestingConfig


@pytest.fixture()
def app():
    app = create_app(TestingConfig)

    # other setup can go

    yield app

    # clean up / reset resources


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()
