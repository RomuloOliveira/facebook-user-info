facebook-user-info
==================

A webservice that collects and offers Facebook user infos through a REST api

### API Documentation

Please see [this link](./docs/api.md) for documentation.

### Environment

Requires: 
- [Python 2.7](https://www.python.org/download/releases/2.7/)
- [MongoDB](http://www.mongodb.org/), for database
- [virtualenv](http://virtualenv.readthedocs.org/en/latest/)

### Dependencies

- [Flask](http://flask.pocoo.org/), for API
- [Flask WTForms](https://wtforms.readthedocs.org/en/latest/), for multipart/form-data requests
- [Mongoengine](http://mongoengine.org/), a ODM (ORM for documents) to make our life easy
- [Requests](http://docs.python-requests.org/), to make our life even easier
- [flake8](https://pypi.python.org/pypi/flake8), to keep the code safe, clean and sane

The script `./bin/build.sh` already install all Python dependencies

### Instructions

#### First steps

1. Configure virtualenv

```bash
$ virtualenv venv
```

2. Activate virtualenv

```bash
$ source venv/bin/activate
```

#### Environment

We provide three environments: `devel`, `test` and `prod`. The default environment is `devel`.  
They are defined in `env` folder, each one in a file.
Each environment defines a set of variables used in the web service.  
  
To change the default environment:
```bash
$ export DEFAULT_ENV=devel|test|prod
```

Additionally, you can use your own environment, called `local` (file `env/local`).  
In this environment, you don't need to define every variable again, only vars that you want.

#### How to run

```bash
$ ./bin/run.sh
```

#### How to test

```bash
$ ./bin/test.sh
```

#### How to lint

```bash
$ ./bin/lint.sh
```

#### How to check test coverage

```bash
$ ./bin/coverage.sh
```

Example output (updated on Oct 16 2014, 7:45PM):
```
(...)
----------------------------------------------------------------------
Ran 5 tests in 0.635s

OK
Name                      Stmts   Miss  Cover
---------------------------------------------
project/__init__             25      2    92%
project/api/__init__          1      0   100%
project/api/person           51     10    80%
project/forms/__init__        0      0   100%
project/forms/person          5      0   100%
project/models/__init__       0      0   100%
project/models/person         7      0   100%
tests/__init__                0      0   100%
tests/api/__init__            0      0   100%
tests/api/test_person        31      0   100%
tests/run                     4      0   100%
---------------------------------------------
TOTAL                       124     12    90%
```

For more info, open `htmlcov/index.html` in a browser. Clicking on modules shows which lines are missing coverage.

### Logging

All server requests, API calls and exceptions are logged. Server requests log uses [Apache's Common Log Format](http://httpd.apache.org/docs/1.3/logs.html#common).  
Example:
```
127.0.0.1 - - [16/Oct/2014 19:05:47] "GET / HTTP/1.1" 404 -
127.0.0.1 - - [16/Oct/2014 19:07:15] "GET /person HTTP/1.1" 200 -
```
  
Errors and exceptions (logged using `app.logger`) use a custom format: `%(asctime)s - %(levelname)s - [%(pathname)s:%(lineno)d] - %(message)s` (See [this](https://docs.python.org/2/library/logging.html#logrecord-attributes) for more details).  
Example:
```
2014-10-16 18:42:06,354 - CRITICAL - [/home/romulo/projects/facebook-user-info/project/api/person.py:76] - Testing
2014-10-16 18:51:09,413 - ERROR - [/home/romulo/projects/facebook-user-info/project/api/person.py:76] - Testing
Traceback (most recent call last):
  File "/home/romulo/projects/facebook-user-info/project/api/person.py", line 74, in add_user
    raise Exception('Testing')
Exception: Testing
```
By default, loggs are saved on `./tmp/info.log` (all levels) and `./tmp/error.log` (_ERROR_ and _CRITICAL_ levels).  
You can change it by setting `LOG_FILE` and `ERROR_LOG_FILE` variables.

### Troubleshooting

**Cannot install some dependencies**  
Check if `virtualenv` is installed, configured and activated (`virtualenv venv; source venv/bin/activate`)
