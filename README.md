# SWAPI

This repo was made as a solution to B2W's challenge Star Wars API.

## Requirements

- Python 3 (*Recommended: 3.6.6*)
- MongoDB Host

Used technologies:

* mongoengine
* flask-restful
* requests (*For SWAPI*)

## Installation

(The use of a virtual environment is totally encouraged)
First of all, use `app.cfg` or `.env` files to configure your settings.
Then, run the following commands:

```
pip install -r requirements.txt     # Download dependencies
python main.py                      # Run server
```

A minimal Dockerfile is also available to standard this process.

## Usage

> ### /api/planets
> GET: Returns list of planets in API's database.
> POST: Creates a new planet.

> ### /api/planets/<id>
> GET: Returns the planet referenced by <id>
> DELETE: Deletes the planet referenced by <id>

## Running tests

Execute:

```
pytest
```

This will start a detailed test, running all tests from `tests/` directory