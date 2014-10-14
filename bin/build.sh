#!/bin/bash

set -e

. bin/clean.sh

pip install -r requirements.txt

. bin/configure.sh
. bin/lint.sh
