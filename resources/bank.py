from flask import current_app as app
from flask_restful import Resource
from utils.exception_handler import handle_exceptions
from functionality.bank_info import get_bank_info, post_bank_info, put_bank_info, delete_bank_info
from webargs.flaskparser import use_kwargs
from marshmallow import Schema, fields as f
from models import session


class BankPostSchema(Schema):
    name = f.Str(required=True)
    address = f.Str(required=True)
    mobile_number = f.Int(required=True)
    bank_manager = f.Str(required=True)

    class Meta:
        strict = True


class BankGetSchema(Schema):
    bank_id = f.Str(required=False)

    class Meta:
        strict = True


class BankPutSchema(Schema):
    bank_id = f.Int(required=True)
    name = f.Str(required=False)
    address = f.Str(required=False)
    mobile_number = f.Int(required=False)
    bank_manager = f.Str(required=False)


class BankDeleteSchema(Schema):
    bank_id = f.Int(required=True)


class BankInfo(Resource):
    decorators = [handle_exceptions]

    def __init__(self):
        app.logger.info('In the constructor of {}'.format(self.__class__.__name__))

    @use_kwargs(BankGetSchema)
    def get(self, **kwargs):
        app.logger.info('In get method of bank info')
        response = get_bank_info(kwargs.get('bank_id'))
        return response

    @use_kwargs(BankPostSchema)
    def post(self, **kwargs):
        app.logger.info("IN Post method of Bank info with parameters {}".format(kwargs))
        response = post_bank_info(**kwargs)
        session.commit()
        return response

    @use_kwargs(BankPutSchema)
    def put(self, **kwargs):
        app.logger.info("In Put method of Bank info with parameter {}".format(kwargs))
        response = put_bank_info(**kwargs)
        session.commit()
        return response

    @use_kwargs(BankDeleteSchema)
    def delete(self, **kwargs):
        app.logger.info("In delete method of Bank info parameter {}".format(kwargs))
        response = delete_bank_info(kwargs.get("bank_id"))
        session.commit()
        return response
