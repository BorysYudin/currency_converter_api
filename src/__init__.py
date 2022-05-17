from flask import Flask

from src import config


def create_app(test_config=None):
    app = Flask(config.APP_NAME, instance_relative_config=True)

    if test_config:
        app.config.from_mapping(test_config)
    else:
        app.config.from_object('src.config')

    register_blueprints(app)

    return app


def register_blueprints(app):
    register_converter_blueprint(app)


def register_converter_blueprint(app):
    from .api import converter
    app.register_blueprint(converter.blueprint)
    app.add_url_rule('/convert_currency', endpoint='convert_currency')
    app.add_url_rule('/latest_rates', endpoint='latest_rates')
