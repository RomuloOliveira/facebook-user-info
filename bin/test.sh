#!/bin/bash

set -e

export ENV=test

. bin/build.sh

python tests/run.py
