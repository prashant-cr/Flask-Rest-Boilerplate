from flask import current_app as app
from flask_restful import Resource
from utils.exception_handler import handle_exceptions


class HealthCheck(Resource):
    decorators = [handle_exceptions]

    def __init__(self):
        app.logger.info('In the constructor of {}'.format(self.__class__.__name__))

    def get(self):
        app.logger.info('Health Check get api called')
        return True