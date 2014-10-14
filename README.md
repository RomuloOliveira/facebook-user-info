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

TODO
```bash
```

### Troubleshooting

**Cannot install some dependencies**  
Check if `virtualenv` is installed, configured and activated (`virtualenv venv; source venv/bin/activate`)
