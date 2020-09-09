from functools import wraps
from flask_restful import abort
from werkzeug.exceptions import UnprocessableEntity
from flask import current_app as app
from models import session
from sqlalchemy.exc import SQLAlchemyError, IntegrityError


class AlreadyExists(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message


class NotFoundError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message


class SessionException(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message


def handle_exceptions(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        try:
            return fn(*args, **kwargs)
        except ValueError as message:
            app.logger.error(message)
            session.rollback()
            return abort(400, message=str(message))
        except KeyError as key_err:
            app.logger.error(key_err)
            session.rollback()
            return abort(400, message=str(key_err))
        except NotFoundError as nf_err:
            app.logger.error(nf_err.message)
            session.rollback()
            return abort(404, message=str(nf_err))
        except IOError as io_err:
            app.logger.error(io_err)
            session.rollback()
            return abort(500, message="IO-ERROR")
        except IntegrityError as err:
            app.logger.error(err)
            session.rollback()
            abort(500, message=str(err))
        except SQLAlchemyError as sa_err:
            app.logger.error(sa_err)
            session.rollback()
            abort(500, message="ORM-ERROR")
        except UnprocessableEntity as sa_err:
            app.logger.error(sa_err)
            session.rollback()
            try:
                message = sa_err.data.get("messages", None)
            except Exception as sa_err:
                message = sa_err
            abort(422, message=str(message))
        except AlreadyExists as err:
            app.logger.error(err.message)
            session.rollback()
            abort(409, message=str(err.message))
        except SessionException as exc:
            app.logger.error(exc.message)
            session.rollback()
            abort(401, message=str(exc.message))
        except Exception as exc:
            app.logger.error(exc)
            session.rollback()
            abort(500, message="INTERNAL-ERROR")

    return wrapper
