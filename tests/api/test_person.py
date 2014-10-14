#!/bin/env python
# -*- coding: utf-8 -*-

import unittest
import json

from project import app

class PersonTest(unittest.TestCase):
    """Test class for /person RESTful resource"""

    def setUp(self):
        app.config['TESTING'] = True
        self.client = app.test_client()

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
