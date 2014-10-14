#!/bin/env python
# -*- coding: utf-8 -*-

from flask.ext.wtf import Form
from wtforms import validators
from wtforms.fields import *

class PersonForm(Form):
    """Person form definition

    Used in POST /person
    """
    facebook_id = StringField('Facebook id', [validators.required()])
