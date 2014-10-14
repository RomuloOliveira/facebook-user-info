#!/bin/env python
# -*- coding: utf-8 -*-

import requests

from project import app
from project.forms.person import PersonForm
from project.models.person import Persons

from flask import request, Response

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

        #
        # Remarks:
        # We are explicitly retrieving a Person document and then saving
        # We could just update the collection, without any validation
        # However, let's use an advantage from our ODM: schema validation
        #

        try:
            # Try to get existent person
            person = Persons.objects.get(facebook_id=person_info['facebook_id'])
        except Persons.DoesNotExist:
            # Create a new Person instance
            person = Persons(facebook_id=person_info['facebook_id'])

        person.name = person_info['name']
        person.facebook_id = person_info['facebook_id']
        person.gender = person_info['gender']
        person.username = person_info['username']

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
    limit_str = request.args.get('limit')

    if limit_str is None: # Retrieve all
        limit = None
    else:
        try:
            limit = int(limit_str)

            if limit < 0:
                raise ValueError('Out of range')
        except ValueError: # not a number
            return '', 400

    persons = Persons.objects()[:limit].exclude('id')

    return Response(persons.to_json(), mimetype='application/json; charset=utf-8')


@app.route('/person/<facebook_id>', methods=['DELETE'])
def delete_user(facebook_id):
    pass
