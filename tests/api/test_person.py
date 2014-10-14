#!/bin/env python
# -*- coding: utf-8 -*-

import unittest

from project import app

class PersonTest(unittest.TestCase):
    """Test class for /person RESTful resource"""

    def setUp(self):
        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_index(self):
        res = self.client.get('/')
        self.assertEquals(res.status_code, 200)

    def test_add(self):
        data = {
            'facebook_id': '100007710667474'
        }

        res = self.client.post('/person', data=data)
        self.assertEquals(res.status_code, 201)

    def test_try_add_not_valid(self):
        data = {
            'wrong_parameter': '123456'
        }

        res = self.client.post('/person', data=data)
        self.assertEquals(res.status_code, 400)
