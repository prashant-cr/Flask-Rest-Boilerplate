from sqlalchemy.orm import scoped_session
from .sessions import DbSession
from config import DATABASE_URL

session = None
session_obj = None


def _get_db_session_obj(database_url):
    global session_obj
    session_obj = DbSession(
        database_url=database_url,
        pool_pre_ping=True,
        pool_recycle=3600,
        pool_size=20,
        max_overflow=10
    )
    return session_obj


def get_session(database_url):
    db_session_obj = _get_db_session_obj(database_url)
    global session
    session = scoped_session(db_session_obj.get_session_factory())
    return session


session = get_session(DATABASE_URL)


