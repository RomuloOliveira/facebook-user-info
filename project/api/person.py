#!/bin/env python
# -*- coding: utf-8 -*-

import requests

from project import app
from project.forms.person import PersonForm
from project.models.person import Persons

from flask import request

def retrieve_person_info(facebook_id):
    """Retrieves a person info based on a facebook id

    Information retrieved:
        facebook_id
        username
        name
        gender

    Returns a dict
    """
    base_url = 'http://graph.facebook.com'
    person_info_url = '{}/{}'.format(base_url, facebook_id)

    r = requests.get(person_info_url).json()

    info = {
        'facebook_id': facebook_id,
        'name': r['name'],
        'gender': r['gender'],
        'username': r['username']
    }

    return info

@app.route('/person', methods=['POST'])
def add_user():
    form = PersonForm(request.form)

    if form.validate_on_submit():
        try:
            person_info = retrieve_person_info(form.facebook_id.data)
        except Exception:
            return '', 400

        person = Persons(
            name=person_info['name'], facebook_id=person_info['facebook_id'],
            gender=person_info['gender'], username=person_info['username']
        )

        # Validate before save
        try:
            person.validate()
        except Exception:
            return '', 400

        try:
            person.save()
        except Exception:
            return '', 500 # We return 500 because not saving it's our fault

        return '', 201

    return '', 400

@app.route('/person', methods=['GET'])
def list_users():
    pass

@app.route('/person/<facebook_id>', methods=['DELETE'])
def delete_user(facebook_id):
    pass
