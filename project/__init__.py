#!/bin/env python
# -*- coding: utf-8 -*-

import os
import logging
import mongoengine

from flask import Flask

app = Flask(__name__)

# I didn't like this code in a function, but it's looks better
def setup_log():
    """Setups logging stuff

    Add a file handler to default Flask Logger (http://stackoverflow.com/a/16743284)
    and an error handler for error, critical and exceptions.
    """

    # Add file handler to default Flask Logger.
    # Reference: http://stackoverflow.com/a/16743284 (Answer #16743284)
    info_logger = logging.FileHandler(os.environ['LOG_FILE'])
    logging.getLogger('werkzeug').addHandler(info_logger)

    # Add error level file handler to our application logger
    error_logger = logging.FileHandler(os.environ['ERROR_LOG_FILE'])
    error_logger.setLevel(logging.ERROR)

    format_str = '%(asctime)s - %(levelname)s - [%(pathname)s:%(lineno)d] - %(message)s'
    formatter = logging.Formatter(format_str)
    error_logger.setFormatter(formatter)

    app.logger.addHandler(error_logger)

if 'DEVEL' in os.environ and os.environ['DEVEL']:
    app.debug = True
    app.config.update(PROPAGATE_EXCEPTIONS=True)

if 'TEST' in os.environ and os.environ['TEST']:
    app.config['TESTING'] = True
    app.config.update(PROPAGATE_EXCEPTIONS=True)

app.config['CSRF_ENABLED'] = False
app.config['WTF_CSRF_ENABLED'] = False

setup_log()

mongoengine.connect(os.environ['DATABASE_NAME'], host=os.environ['DATABASE_HOST'])

# We need 'app' on this modules, so we import only here
from project.api import *
