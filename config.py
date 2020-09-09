import os
import sys
import logging
import pwd

BASE_PATH = pwd.getpwuid(os.getuid()).pw_dir

DATABASE_URL = os.environ.get("DATABASE_URL")
DEFAULT_LOGGER_NAME = os.environ.get("DEFAULT_LOGGER_NAME")
os.environ["DEBUG"] = os.environ.get("BACKEND_DEBUG")
APP_LOG_FILE = 'logs/'


FILE_LOG_CONFIG = {
    'filename': 'loggDATA_BACKEND_SESSION_URLing.log',
    'loglevel': logging.DEBUG,
    'local_logdir_path': APP_LOG_FILE,
    'formatter_string': '%(request_id)s - %(asctime)s - %(filename)s - %(module)s - %(funcName)s - %(lineno)d - '
                        '[%(levelname)s] - %(message)s',
    'kwargs': {
        'utc': True
    }
}
LOGGING_CONFIG = dict(
    version=1,
    filters={
        'request_id': {
            '()': 'utils.logger.RequestIdFilter',
        },
    },
    formatters={
        'compact': {
            'format': '%(asctime)s [%(levelname)s] %(name)-10.10s : %(message)s'
        },
        'verbose': {
            'format': '%(request_id)s - %(asctime)s - %(filename)s - %(module)s - %(funcName)s - '
                      '%(lineno)d - [%(levelname)s] - %(message)s'
        },
        'err_report': {'format': '%(asctime)s\n%(message)s'}
    },
    handlers={
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'stream': sys.stdout,
            'formatter': 'compact',
            'filters': ['request_id']
        },
        DEFAULT_LOGGER_NAME: {
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'verbose',
            'filters': ['request_id'],
            'level': 'DEBUG',
            'filename': APP_LOG_FILE
        },
        'critical_err': {
            'class': 'logging.handlers.SMTPHandler',
            'formatter': 'err_report',
            'mailhost': ("localhost", 25),
            'fromaddr': 'no-reply@onehop.co',
            'toaddrs': [
                "ketan.pise@screen-magic.com"
            ],
            'subject': 'Tenjin Data API : Something bad happened'
        }
    },
    loggers={
        DEFAULT_LOGGER_NAME: {
            'handlers': [DEFAULT_LOGGER_NAME, 'console'],
            'level': 'DEBUG',
            'propagate': False
        },
        'crash': {
            'handlers': [DEFAULT_LOGGER_NAME],
            'level': 'ERROR',
            'propagate': False
        },
    }
)

