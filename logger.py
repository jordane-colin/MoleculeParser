#!/usr/bin/env python3

import logging.config
import os


def get_logger():
    # set log level from env variable
    log_level = os.environ.get('LOG_LEVEL', 'INFO').upper()
    logging.basicConfig(level=log_level)
    logging.config.fileConfig('./logging.ini',
                              disable_existing_loggers=False,
                              defaults={'level': log_level})
    logger = logging.getLogger(__name__)

    return logger
