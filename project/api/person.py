#!/bin/env python
# -*- coding: utf-8 -*-

from project import app
from project.forms import person

from flask import request

@app.route('/person', methods=['POST'])
def add_user():
    form = person.PersonForm(request.form)

    if form.validate_on_submit():
        return '', 201

    return '', 400

@app.route('/', methods=['GET'])
def index():
    return 'hello'
