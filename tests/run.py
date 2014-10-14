#!/bin/env python
# -*- coding: utf-8 -*-

import unittest

if __name__ == '__main__':
    suite = unittest.TestLoader().discover('.')
    unittest.TextTestRunner().run(suite)
