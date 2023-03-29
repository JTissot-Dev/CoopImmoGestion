import os

from flask import Flask
from .db.db import db, migrate
from .config.DevelopmentConfig import DevelopmentConfig
from .config.ProductionConfig import ProductionConfig
from .config.TestingConfig import TestingConfig


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)

    if test_config is None:
        # Set production config when app is deployed
        if os.environ.get('FLASK_ENV') == 'production':
            app.config.from_object(ProductionConfig)
        # Set testing config for test db migration
        if os.environ.get('FLASK_ENV') == 'testing':
            app.config.from_object(TestingConfig)
    else:
        # load the test config for unit test pytest
        app.config.from_object(test_config)

    @app.route('/connexion', methods=["POST"])
    def initialization():
        return 'Flask initialization'

    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        db.create_all()

    return app
