#!/bin/env python
# -*- coding: utf-8 -*-

import unittest
import json

from project import app

class PersonTest(unittest.TestCase):
    """Test class for /person RESTful resource"""

    # Class variable
    test_facebook_id = '100007710667474'

    def setUp(self):
        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_add(self):
        data = {
            'facebook_id': self.test_facebook_id
        }

        res = self.client.post('/person', data=data)
        self.assertEquals(res.status_code, 201)

    def test_stupid_add(self):
        data = {
            'facebook_id': 'blah'
        }

        res = self.client.post('/person', data=data)
        self.assertEquals(res.status_code, 400)

    def test_try_add_not_valid(self):
        data = {
            'wrong_parameter': '123456'
        }

        res = self.client.post('/person', data=data)
        self.assertEquals(res.status_code, 400)

    def test_list_limit(self):
        limit = 50
        res = self.client.get('/person?limit={}'.format(limit))
        self.assertEquals(res.status_code, 200)

        json_res = json.loads(res.data)

        self.assertIsInstance(json_res, list)
        self.assertTrue(len(json_res) <= limit)

    def test_list_without_limit(self):
        res = self.client.get('/person')
        self.assertEquals(res.status_code, 200)

        json_res = json.loads(res.data)

        self.assertIsInstance(json_res, list)

    def test_list_wrong_limit(self):
        limit = -1
        res = self.client.get('/person?limit={}'.format(limit))
        self.assertEquals(res.status_code, 400)

    def test_delete(self):
        self.test_add()

        res = self.client.delete('/person/{}'.format(self.test_facebook_id))
        self.assertEquals(res.status_code, 204)

    def test_fail_delete(self):
        res = self.client.delete('/person/{}'.format('some_fucking_random_id'))
        self.assertEquals(res.status_code, 404)

    def test_delete_invalid_params(self):
        res = self.client.delete('/person')
        self.assertEquals(res.status_code, 405)

        res = self.client.delete('/person/')
        self.assertEquals(res.status_code, 404)
