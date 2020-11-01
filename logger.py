#!/usr/bin/env python3

import logging.config
import os


def get_logger():
    # set log level from env variable
    LOG_LEVEL = os.environ.get('LOG_LEVEL', 'INFO').upper()
    logging.basicConfig(level=LOG_LEVEL)
    logging.config.fileConfig('./logging.ini', disable_existing_loggers=False, defaults={'level': LOG_LEVEL})
    logger = logging.getLogger(__name__)

    return logger