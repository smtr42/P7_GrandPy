"""Set up a simple logger for the application"""
import logging
from logging.handlers import RotatingFileHandler


def setup_logger():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        '%(asctime)s [%(levelname)s] | File \"%(filename)s\" in \"%('
        'funcName)s\" line %(lineno)s: %(message)s')

    file_handler = RotatingFileHandler('logger/log/activity.log',
                                       'a',
                                       10000000,
                                       1
                                       )

    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    return logger, stream_handler


logger, stream_handler = setup_logger()
