from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker
from .ping import ping_connection


class DbSession:
    def __init__(self, **kwargs):
        self.database_url = kwargs.pop("database_url")
        self.pool_pre_ping = kwargs.pop("pool_pre_ping", False)
        self.kwargs = kwargs
        self.factory, self.session = None, None

    def get_session(self):
        if self.session:
            return self.session

        factory = self.get_session_factory()
        self.session = factory()
        return self.session

    def get_session_factory(self):
        if self.factory:
            return self.factory

        db_engine = create_engine(self.database_url, **self.kwargs)

        # http://docs.sqlalchemy.org/en/latest/core/pooling.html
        if self.pool_pre_ping:
            event.listen(db_engine, "engine_connect", ping_connection)

        db_session_factory = sessionmaker(
            bind=db_engine)
        self.factory = db_session_factory

        return self.factory
