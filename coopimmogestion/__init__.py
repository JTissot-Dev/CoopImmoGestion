import os

from flask import Flask
from .db.db import db, migrate
from .config.DevelopmentConfig import DevelopmentConfig
from .config.ProductionConfig import ProductionConfig


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)

    if test_config is None:
        if os.environ.get('FLASK_ENV') == 'production':
            app.config.from_object(ProductionConfig)
    else:
        # load the test config if passed in
        app.config.from_object(test_config)

    @app.route('/')
    def initialization():
        return 'Flask initialization'

    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        db.create_all()

    return app
