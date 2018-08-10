"""
API Module
"""
import logging
import pkgutil
import importlib

from flask import Blueprint
from flask_restplus import Api

import config

LOG = logging.getLogger(__name__)


def create_module():
    """
    Entry point to the module
    """
    blueprint = Blueprint('api', __name__, url_prefix='/api')
    api = Api(blueprint,
              title='Generic API',
              version='0.1',
              description='Test API to use',
              )

    api.namespaces.pop(0)  # Remove default namespace

    @api.errorhandler  # pragma: no cover
    def default_error_handler():  # pylint: disable=unused-variable
        message = 'An unhandled exception occurred.'
        LOG.exception(message)

        if not config.BaseConfig.FLASK_DEBUG:
            return {'message': message}, 500

        return None, 500

    # Register all submodules (namespaces)
    for module_loader, name, ispkg in pkgutil.iter_modules(  # pylint: disable=unused-variable
            path=__path__, prefix=__name__ + '.'):
        api.add_namespace(importlib.import_module(name).api)

    LOG.info('Module created')
    return blueprint
