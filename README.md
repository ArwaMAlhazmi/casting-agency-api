# Casting Agency API

## Table of Contents

* [Overview](#Overview)
* [Getting Started](#Getting_Started)
* [Running the Server Locally](Running_the_Server_Locally)
* [Testing](Testing)
* [API Reference](API_Reference)

## Overview
Udacity FSND - Casting Agency API Capstone
SQLAlchemy ORM, PostgreSQL, Python3, Flask, CORS, RBAC, Auth0, Unittest

### Motivation
This capstone was developed for Udacity FSND, It covers all of the concepts and the skills to build an API from start to finish and host it.
The Casting Agency api models a company that is responsible for creating movies and managing and assigning actors to those movies. The Casting Agency API is a system to simplify and streamline the company's process.


## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

It is recommended to work within a virtual environment whenever using Python for projects. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

With virtual environment setup and running, install dependencies by running:

```bash
pip3 install -r requirements.txt
```
This will install all of the required packages we selected within the `requirements.txt` file.


## Running the Server Locally

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
To run the tests, you need to restore the test database first. 
Run the following commands in order:
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
  1. Import the postman collection `udacity-fsnd-castingagencyapi.postman_collection` 
  2. Run the collection. 
  * Each folder(Casting Assistant, Casting Director, Executive Producer) has a description for tha expected response for each request based on the role of the user making the request.
  
  * You can use the following tokens to make your own calls to the api:

  EXCTIVE_PRODUCER: "permissions": ["delete:actors", "delete:movies", "get:actors", "get:movies", "patch:actors", 
  "patch:movies", "post:actors", "post:movies"]
  ```
  EXCTIVE_PRODUCER_JWT=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Im0xY2dtbWo4QjdQTmhkSzd0R25idiJ9.eyJpc3MiOiJodHRwczovL2Rldi1uaDFlanY5MC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWZjOThlMDI0ZTJhZDEwMDcxNTlkNDdmIiwiYXVkIjoiY2FzdGluZyIsImlhdCI6MTYxMTY4NjU2OCwiZXhwIjoxNjExNzcyOTY4LCJhenAiOiJqQmh1RE05NjRLOUIyTUIzR1M2N0ZBTjFkOTd4UEYwMyIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIiwicG9zdDptb3ZpZXMiXX0.c3agGbeILQN3h0sKl4qp_bhyeKbpB_3_6ejdidiYwux9zps8kVLQjHzPi5Nvp3tNRUWCZUBBUv5QijXdd0Bv1gGuacGz8NxpWgc3eRsE3W_pSebGQltfGx-u9bnCVGY26UZyYjyswpruhaboCCB72Q3qVDWhVUfVnte8RkZmya3pxUosWJBss1gs6gQnNpl9ROXexdlPQqd-bJ-PS0JzjprgZl0H_MvffS2PNC7iL9CvqnZfoRcmVNwVvdMR7mIxoUPUUCmP49iZu2CeOViI-AQRhGBdg9nXcr8wcwHVl3wRV2qBHZCwFzWx57MqYMTQezn2K5uDHmrcqwCNbMTnFA
  ```

  CASTING_DIRECTOR:  "permissions": ["delete:actors", "get:actors", "get:movies", "patch:actors", "patch:movies", "post:actors"]
   ```
  CASTING_DIRECTOR_JWT=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Im0xY2dtbWo4QjdQTmhkSzd0R25idiJ9.eyJpc3MiOiJodHRwczovL2Rldi1uaDFlanY5MC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWZjOThlOGFjMDU4ZjgwMDZmNDIxMWQzIiwiYXVkIjoiY2FzdGluZyIsImlhdCI6MTYxMTY4Njg0OSwiZXhwIjoxNjExNzczMjQ5LCJhenAiOiJqQmh1RE05NjRLOUIyTUIzR1M2N0ZBTjFkOTd4UEYwMyIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiXX0.UKBFebG9gcrgeMmr_SbAauO_0jKfAZE9nhm5Mk1FR_MmJH7lHIgirE4_uOSxMtdd2nxfkI4Re5c9ALtvO0uC0aTRmrzJkjcgFM06idfZEK1V9rCFgoyeYkIsspnqNUJAuXBmnPSE7L9BUahHLQacGARbiRxRiSJD57MLj9ajvTJcV33UDImohFkmxiVj66Esi2_aEZzTvsywevKLsJCjV4v01aPCwSqwLoTLbC9uUOC5Wn3O-7xT6ZCJGruPmTGGeYo8nHKthF85ZO7qGSezgc-gXFpKIY5xDWXHfo_j5Gr4z8aFyDBoiQm9wodUYES2ncuSv2NVZLodFI7q5QqVXQ
   ```

   CASTING_ASSISTANT: "permissions": ["get:actors", "get:movies"]
   ```
   CASTING_ASSISTANT_JWT=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Im0xY2dtbWo4QjdQTmhkSzd0R25idiJ9.eyJpc3MiOiJodHRwczovL2Rldi1uaDFlanY5MC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWZjZDBiNjdmNDQwYzAwMDZlMWZlZjJkIiwiYXVkIjoiY2FzdGluZyIsImlhdCI6MTYxMTY4NjkzOSwiZXhwIjoxNjExNzczMzM5LCJhenAiOiJqQmh1RE05NjRLOUIyTUIzR1M2N0ZBTjFkOTd4UEYwMyIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiXX0.GRTep-aPydUpOa6yyA7iqOTVcTz8OFuqhaLxpZg2MfW8qQYsGwTS6w6uBNl0EKKa0nVyvZbsAhzq98bTifd7zxGsL4FEQ6e4Wky_V77beMaJcY5KAtlEHyCwxn11igQw1mU6v37ONozImBt5e-3_pivMWHwO_a_8uEuVqeGjTVk31xeZ1K9ylCUgNxqqhSwbP0teo0uey4uRFdUk2anpNlrmj6sUD8Z9GGdKP7Dr3MCaZfMY2T-9PMqYnfP3Yp5AjNq4B_IyLyzmWJDpldXsRDimCG-6MR8vOjHqmvZygJ7kJTsn9VQ1vqe5gEF144Gp-dI9E8PpuIz4fU7DeEwsuQ
   ```


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