#!/bin/env python
# -*- coding: utf-8 -*-

import os
import mongoengine

from flask import Flask

app = Flask(__name__)

if 'DEVEL' in os.environ and os.environ['DEVEL']:
    app.debug = True
    app.config.update(PROPAGATE_EXCEPTIONS=True)

if 'TEST' in os.environ and os.environ['TEST']:
    app.config['TESTING'] = True
    app.config.update(PROPAGATE_EXCEPTIONS=True)

app.config['CSRF_ENABLED'] = False
app.config['WTF_CSRF_ENABLED'] = False

mongoengine.connect(os.environ['DATABASE_NAME'], host=os.environ['DATABASE_HOST'])

# We need 'app' on this modules, so we import only here
from project.api import *
