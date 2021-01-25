# Casting Agency API

## Table of Contents

* [Overview](#Overview)
* [Getting Started](#Getting_Started)

## Overview
Udacity FSND - Casting Agency API Capstone
SQLAlchemy ORM, PostgreSQL, Python3, Flask, CORS, RBAC, Auth0, Unittest

The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies. The Casting Agency API is a system to simplify and streamline the company's process.

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

It is recommended to work within a virtual environment whenever using Python for projects. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

With virtual environment setup and running, install dependencies by running:

```bash
pip install -r requirements.txt
```
This will install all of the required packages we selected within the `requirements.txt` file.


## Running the server Locally

From within the project directory first ensure you are working using your created virtual environment.

1. clone the project

```bash
git clone https://github.com/ArwaMAlhazmi/casting-agency-api.git
```

2. To run the server, execute:

```bash
source setup.sh
dropdb castingagencydb
createdb castingagencydb
psql castingagencydb < castingagency_test.psql
flask run --reload
```

## Testing
To run the tests, run
```
source setup.sh
dropdb castingagency_test
createdb castingagency_test
psql castingagency_test < castingagency_test.psql
py test_app.py
```

## API Reference

### Getting Started
- Base URL:
 * The api can be run locally. The app is hosted at the default, `http://127.0.0.1:5000/`.
 * The api is also hosted at: https://casting-agancy-api.herokuapp.com/hello

- Authentication: Auth0 api is used for authenticating. 
  The endpoints can be requested with [Postman](https://getpostman.com). 
  1. Import the postman collection `./starter_code/backend/udacity-fsnd-udaspicelatte.postman_collection.json` 
  2. Run the collection. 
  * Each folder(Casting Assistant, Casting Director, Executive Producer) has a description for tha expected response for each request based on the role of the user making the request.


### Error Handling
Errors are returned as JSON objects in the following format:
```
{
    "success": False, 
    "error": 400,
    "message": "bad request"
}
```
The API will return three error types when requests fail:
- 400: Bad Request
- 404: Resource Not Found
- 422: Not Processable
- 401: Header error message
- 403: Autherization error message

### Endpoints 
#### GET /movies
  Returns a list of movies and success value
```
{
    "movies": [
        {
            "id": 2,
            "release_date": "Tue, 01 Jan 2019 00:00:00 GMT",
            "title": "Avengers: Endgame"
        },
        {
            "id": 3,
            "release_date": "Mon, 01 Jan 2018 00:00:00 GMT",
            "title": "Avengers: Infinity War"
        },
        {
            "id": 4,
            "release_date": "Thu, 01 Jan 2015 00:00:00 GMT",
            "title": "Avengers: Age of Ultron"
        }
    ],
    "success": true
}
```

#### GET /actors
  Returns a list of actors and success value
```
{
    "actors": [
        {
            "age": 28,
            "gender": "female",
            "id": 3,
            "name": "lily James"
        },
        {
            "age": 55,
            "gender": "male",
            "id": 4,
            "name": "Robert Downey, Jr."
        },
        {
            "age": 36,
            "gender": "female",
            "id": 5,
            "name": "Scarlett Johansson"
        }
    ],
    "success": true
}
```

#### DELETE /movies/{movie_id}
  Deletes the movie of the given ID if it exists. Returns the id of the deleted movie and success value
```
{
  "deleted": 1,
  "success": true
}
```

#### DELETE /actors/{actor_id}
  Deletes the actor of the given ID if it exists. Returns the id of the deleted actor and success value
```
{
  "deleted": 1,
  "success": true
}
```

#### POST /movies
  (body contains movie data) Creates a new movie using the submitted movie title, and release date. Returns a success value.
```
{
  "success": true
}
```

#### POST /actor
  (body contains actor data) Creates a new actor using the submitted actor name, age, and gender. Returns a success value.
```
{
  "success": true
}
```

#### PATCH /movies/{movie_id}
  (body contains movie data) Updates the movie of the given ID if it exists. Returns the updated movie object and success value
```
{
    "movie": {
        "id": 1,
        "release_date": "Fri, 01 Mar 2019 00:00:00 GMT",
        "title": "'Avengers: Endgame'"
    },
    "success": true
}
```
#### PATCH /actors/{actor_id}
  (body contains actor data) Updates the actor of the given ID if it exists. Returns the updated actor object and success value
```
{
    "actor": {
        "age": 28,
        "gender": "female",
        "id": 3,
        "name": "lily James"
    },
    "success": true
}
```