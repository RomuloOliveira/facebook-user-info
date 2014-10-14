facebook-user-info
==================

A webservice that collects and offers Facebook user infos through a REST api

### API Documentation

Please see [this link](./docs/api.md) for documentation.

### Environment

Requires: 
- [Python 2.7](https://www.python.org/download/releases/2.7/)
- [virtualenv](http://virtualenv.readthedocs.org/en/latest/)

### Dependencies

- [Flask](http://flask.pocoo.org/), for API
- [MongoDB](http://www.mongodb.org/), for database
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
Check if `virtualenv` is installed and activated (`virtualenv venv; source venv/bin/activate`)
