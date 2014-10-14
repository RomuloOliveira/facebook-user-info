#!/bin/env python
# -*- coding: utf-8 -*-

from project import app

from flask import request

from flask.ext.wtf import Form
from wtforms import validators
from wtforms.fields import *

class PersonForm(Form):
    """Person form definition

    Used in POST /person
    """
    facebook_id = StringField('Facebook id', [validators.required()])

@app.route('/person', methods=['POST'])
def add_user():
    form = PersonForm(request.form)

    if form.validate_on_submit():
        return '', 201

    return '', 400

@app.route('/', methods=['GET'])
def index():
    return 'hello'
