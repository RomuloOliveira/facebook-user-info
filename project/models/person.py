#!/bin/env python
# -*- coding: utf-8 -*-

import mongoengine
from mongoengine.fields import *

class Persons(mongoengine.Document):
    """Database model for a Person

    Used in many /person calls
    """
    facebook_id = StringField(required=True)
    username = StringField(required=True)
    name = StringField(required=True)
    gender = StringField(required=True)
