#!/bin/env python
# -*- coding: utf-8 -*-

import os

from project import app

if __name__ == '__main__':
    port = int(os.environ['PORT'])
    app.run(port=port)
