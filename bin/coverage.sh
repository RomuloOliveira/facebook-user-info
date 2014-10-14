#!/bin/bash

set -e

export ENV=test

. bin/build.sh

coverage run tests/run.py

coverage report --omit='venv/*'

coverage html --omit='venv/*'
echo 'For more details, please see "htmlcov/index.html" report'
