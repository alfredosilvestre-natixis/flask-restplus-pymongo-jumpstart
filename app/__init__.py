"""
APP start module
"""
import logging
import pkgutil
import importlib

from flask import Flask
from flask.logging import default_handler
from flask_pymongo import PyMongo

from config import CONFIG_NAME_MAPPER

LOG = logging.getLogger(__name__)


class App:  # pylint: disable=too-few-public-methods
    """
    APP class
    """
    @classmethod
    def __init__(cls):
        cls.mongodb = None

    @classmethod
    def create_app(cls, flask_config_name):
        """
        Entry point to the application
        """
        app = Flask(__name__)
        app.config.from_object(CONFIG_NAME_MAPPER[flask_config_name])

        # Configure root logger with flask app default handler and log level from config
        root = logging.getLogger()
        root.addHandler(default_handler)
        root.setLevel(app.config['LOG_LEVEL'])

        # Add log file handler
        file_handler = logging.FileHandler('app.log')
        file_handler.setFormatter(logging.Formatter(
            '[%(asctime)s] - %(name)s - %(levelname)s - %(message)s'))
        root.addHandler(file_handler)

        cls.mongodb = PyMongo(app)

        # Register all blueprints
        for module_loader, name, ispkg in pkgutil.iter_modules(  # pylint: disable=unused-variable
                path=__path__, prefix=__name__ + '.'):
            app.register_blueprint(importlib.import_module(name).create_module())

        LOG.info('Application started')
        return app
