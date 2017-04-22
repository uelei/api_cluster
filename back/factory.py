from flask import Flask


def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_pyfile(config_filename)

    from back.models import db
    db.init_app(app)

    from back.main import main

    app.register_blueprint(main)
    return app
