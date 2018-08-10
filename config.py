import logging


class BaseConfig:
    SECRET_KEY = 'this-really-needs-to-be-changed'
    DEBUG = False

    # Flask settings
    FLASK_DEBUG = True

    # Flask-Restplus settings
    RESTPLUS_VALIDATE = True
    RESTPLUS_MASK_SWAGGER = False
    RESTPLUS_ERROR_404_HELP = False

    # Logger settings
    LOG_LEVEL = logging.INFO


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    # MongoDB settings
    MONGO_URI = 'mongodb://localhost:27017/dev'


class TestingConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    # MongoDB settings
    MONGO_URI = 'mongodb://localhost:27017/test'


class ProductionConfig(BaseConfig):
    DEBUG = False

    # Flask settings
    FLASK_DEBUG = False

    # MongoDB settings
    MONGO_URI = 'mongodb://localhost:27017/db'


CONFIG_NAME_MAPPER = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
