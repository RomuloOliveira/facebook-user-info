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
