import os
from flask import (Flask, request, abort, jsonify)
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import (setup_db, Movie, Actor)
from auth import (AuthError, requires_auth)


def create_app(test_config=None):
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    '''
	Use the after_request decorator to set Access-Control-Allow
	'''
    @app.after_request
    def after_request(response):
        response.headers.add(
            'Access-Control-Allow-Headers',
            'Content-Type,Authorization,true')
        response.headers.add(
            'Access-Control-Allow-Methods',
            'GET,PUT,POST,DELETE,PATCH,OPTIONS')
        return response

    @app.route('/hello')
    def hello():
        return jsonify({
            "greeting": "hello form casting agency api",
        }), 200

    '''
	GET endpoint to get movies
	'''
    @app.route('/movies')
    @requires_auth('get:movies')
    def retrieve_movies(payload):
        movies = Movie.query.order_by(Movie.id).all()
        formated_movies = [movie.format() for movie in movies]

        return jsonify({
            "success": True,
            "movies": formated_movies
        }), 200

    '''
	GET endpoint to get actors
	'''
    @app.route('/actors')
    @requires_auth('get:actors')
    def retrieve_actors(payload):
        actors = Actor.query.order_by(Actor.id).all()
        formated_actors = [actor.format() for actor in actors]

        return jsonify({
            "success": True,
            "actors": formated_actors
        }), 200

    '''
	DELETE endpoint to delete movie based on movie_id
	'''
    @app.route('/movies/<int:movie_id>', methods=['DELETE'])
    @requires_auth('delete:movies')
    def delete_movie(payload, movie_id):

        movie = Movie.query.filter(Movie.id == movie_id).one_or_none()

        if movie is None:
            abort(404)

        try:
            movie.delete()

            return jsonify({
                'success': True,
                'deleted': movie_id
            }), 200

        except unprocessableEntity:
            abort(422)

    '''
	DELETE endpoint to delete actor based on actor_id
	'''
    @app.route('/actors/<int:actor_id>', methods=['DELETE'])
    @requires_auth('delete:actors')
    def delete_actor(payload, actor_id):

        actor = Actor.query.filter(Actor.id == actor_id).one_or_none()

        if actor is None:
            abort(404)

        try:
            actor.delete()

            return jsonify({
                'success': True,
                'deleted': actor_id
            }), 200

        except unprocessableEntity:
            abort(422)

    '''
	POST endpoint to create a new actor
	'''
    @app.route('/actors', methods=['POST'])
    @requires_auth('post:actors')
    def create_actor(payload):

        body = request.get_json()

        new_name = body.get('name', None)
        new_age = body.get('age', None)
        new_gender = body.get('gender', None)

        try:
            actor = Actor(name=new_name, age=new_age, gender=new_gender)
            actor.insert()

            return jsonify({
                'success': True
            }), 200
        except unprocessableEntity:
            print("aported 422")
            abort(422)

    '''
	POST endpoint to create a new movie
	'''
    @app.route('/movies', methods=['POST'])
    @requires_auth('post:movies')
    def create_movie(payload):

        body = request.get_json()

        new_title = body.get('title', None)
        new_release_date = body.get('release_date', None)

        try:
            movie = Movie(title=new_title, release_date=new_release_date)
            movie.insert()

            return jsonify({
                'success': True,
            }), 200
        except unprocessableEntity:
            abort(422)

    '''
	PATCH endpoint to update an actor based on id
	'''
    @app.route('/actors/<int:actor_id>', methods=['PATCH'])
    @requires_auth('patch:actors')
    def patch_actor(payload, actor_id):

        # Fetch actor to be updated
        actor = Actor.query.filter(Actor.id == actor_id).one_or_none()

        if actor is None:
            abort(404)

        body = request.get_json()
        new_name = body.get('name', None)
        new_age = body.get('age', None)
        new_gender = body.get('gender', None)

        if new_name is None and new_age is None and new_gender is None:
            abort(404)

        if new_name:
            actor.name = new_name
        if new_age:
            actor.age = new_age
        if new_gender:
            actor.gender = new_gender

        try:
            actor.update()

            updated_actor = Actor.query.filter(
                Actor.id == actor_id).one_or_none()
            formatted_actor = updated_actor.format()

            return jsonify({
                'success': True,
                'actor': formatted_actor
            }), 200

        except unprocessableEntity:
            abort(422)

    '''
	PATCH endpoint to update a movie based on id
	'''
    @app.route('/movies/<int:movie_id>', methods=['PATCH'])
    @requires_auth('patch:movies')
    def patch_movie(payload, movie_id):

        # Fetch movie to be updated
        movie = Movie.query.filter(Movie.id == movie_id).one_or_none()

        if movie is None:
            abort(404)

        body = request.get_json()
        new_title = body.get('title', None)
        release_date = body.get('release_date', None)

        if new_title is None and release_date is None:
            abort(404)

        if new_title:
            movie.title = new_title
        if release_date:
            movie.release_date = release_date

        try:

            movie.update()

            updated_movie = Movie.query.filter(
                Movie.id == movie_id).one_or_none()
            formatted_movie = updated_movie.format()
            return jsonify({
                "success": True,
                "movie": formatted_movie
            }), 200
        except unprocessableEntity:
            abort(422)

    '''
	Error Handler
	'''
    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "Unprocessable"
        }), 422

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "Resource Not Found"
        }), 404

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "Bad Request"
        }), 400

    @app.errorhandler(500)
    def internal_server_error(error):
        return jsonify({
            "success": False,
            "error": 500,
            "message": "Internal Server Error"
        }), 500

    @app.errorhandler(401)
    def unotherized(error):
        return jsonify({
            "success": False,
            "error": 401,
            "message": "Unautherized"
        }), 401

    '''
	error handler for AuthError
	'''
    @app.errorhandler(AuthError)
    def handle_auth_error(ex):
        response = jsonify(ex.error)
        response.status_code = ex.status_code
        return response

    return app


APP = create_app()

if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)
