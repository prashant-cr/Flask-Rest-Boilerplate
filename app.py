import resources
from flask import Flask
from models import get_session
from utils.log_utils import config_logger


def create_app():
    app = Flask('data_api_app')
    app.config.from_object('config')

    database_url = app.config.get('DATABASE_URL')
    if not database_url:
        raise Exception("Environment Exception: DATABASE_URL not set.")

    session = get_session(database_url)

    config_logger(app)

    resources.create_api(app)

    def close_session(response_or_exc):
        session.remove()
        return response_or_exc

    app.teardown_request(close_session)
    app.teardown_appcontext(close_session)
    return app


main_app = create_app()

if __name__ == '__main__':
    main_app.run('0.0.0.0', 5009)

