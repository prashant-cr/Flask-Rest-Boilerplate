import unittest

from flask import Flask
from sm_data_models.session import DbSession


class TestFactory(unittest.TestCase):
    def setUp(self):
        super(TestFactory, self).setUp()
        self.maxDiff = None
        self.app = Flask(__name__)
        self.app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:@localhost/smdataapi'
        self.app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
        dbobj = DbSession(database_url=self.app.config["SQLALCHEMY_DATABASE_URI"])
        self.session = dbobj.get_session()

        self.app.config.from_object(__name__)

        import logging
        self.logger = logging.getLogger()
        self.app.app_context().push()  # BIND SQLALCHEMY TO APPLICATION

    def tearDown(self):
        super(TestFactory, self).tearDown()
        self.session.rollback()
        self.session.close()
