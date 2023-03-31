import os

from flask import Flask
from .crypt.crypt import bcrypt
from .db.db import db, migrate
from .config.DevelopmentConfig import DevelopmentConfig
from .config.ProductionConfig import ProductionConfig
from .config.TestingConfig import TestingConfig
from .controller.LoginView import LoginView
from .controller.IndexView import IndexView


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)

    if test_config is None:
        # Set production config when app is deployed
        if os.environ.get('FLASK_ENV') == 'production':
            app.config.from_object(ProductionConfig)
    else:
        # load the test config for unit test pytest
        app.config.from_object(test_config)

    app.add_url_rule('/connexion', view_func=LoginView.as_view('login_view'))
    app.add_url_rule('/', view_func=IndexView.as_view('index_view'))

    bcrypt.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)

    return app
