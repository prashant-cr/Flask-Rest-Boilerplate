from flask_cors import CORS
from flask_restful import Api
from resources.healthcheck import HealthCheck
from .bank import BankInfo


def create_api(app):
    # added cors as it was only giving pre-flight request
    CORS(app, supports_credentials=True, resources={r"/*": {"origins": "*"}})
    api = Api(app, prefix='/api/')
    api.add_resource(HealthCheck, "healthcheck")
    api.add_resource(BankInfo, "bank/info")

