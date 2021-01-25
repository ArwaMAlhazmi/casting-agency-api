import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Actor, Movie

castingAssistantJWT = os.environ['CASTING_ASSISTANT_JWT']
castingDirectorJWT = os.environ['CASTING_DIRECTOR_JWT']
executiveProducerJWT = os.environ['EXCTIVE_PRODUCER_JWT']


class CastingTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "castingagency_test"
        self.database_path = "postgres://{}:{}@{}/{}".format('postgres', 'postgres','localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        self.new_actor = {
            'name': 'Elizabeth Olsen',
            'age': '31',
            'gender': 'female'
        }

        self.new_movie = {
            'title': 'Avengers: Age of Ultron',
            'release_date': '2015-12-31'
        }

        self.patch_age = {
        	'age': 56
        }

        self.patch_date = {
        	'release_date': '2012-01-01'
        }
        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
   
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    tests for successful operation and for expected errors.
    """
    def test_hello(self):
        res = self.client().get('/hello')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)


    def test_post_new_movie(self):
        res = self.client().post('/movies', json=self.new_movie, headers={'Content-Type': 'application/json', 'Authorization': 'Bearer {}'.format(executiveProducerJWT)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_403_not_autherized_post_new_movie(self):
        res = self.client().post('/movies', json=self.new_movie, headers={'Content-Type': 'application/json', 'Authorization': 'Bearer {}'.format(castingDirectorJWT)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['code'], 'unauthorized')

    def test_post_new_actor(self):
        res = self.client().post('/actors', json=self.new_actor, headers={'Content-Type': 'application/json', 'Authorization': 'Bearer {}'.format(castingDirectorJWT)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_403_not_autherized_post_new_actor(self):
        res = self.client().post('/actors', json=self.new_actor, headers={'Content-Type': 'application/json', 'Authorization': 'Bearer {}'.format(castingAssistantJWT)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['code'], 'unauthorized')

    def test_get_movies(self):
        res = self.client().get('/movies', headers={'Content-Type': 'application/json', 'Authorization': 'Bearer {}'.format(castingAssistantJWT)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['movies']))

    def test_401_get_movies_authorization_header_missing(self):
        res = self.client().get('/movies')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['code'], 'authorization_header_missing')

    def test_get_actors(self):
        res = self.client().get('/actors', headers={'Content-Type': 'application/json', 'Authorization': 'Bearer {}'.format(castingAssistantJWT)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['actors']))

    def test_401_get_actors_authorization_header_missing(self):
        res = self.client().get('/actors')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['code'], 'authorization_header_missing')


    def test_patch_actor_age(self):
        res = self.client().patch('/actors/1', json=self.patch_age, headers={'Content-Type': 'application/json', 'Authorization': 'Bearer {}'.format(castingDirectorJWT)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['actor']))

    def test_403_not_autherized_patch_actor_age(self):
        res = self.client().patch('/actors/1', json=self.patch_age, headers={'Content-Type': 'application/json', 'Authorization': 'Bearer {}'.format(castingAssistantJWT)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['code'], 'unauthorized')

    def test_patch_movie_date(self):
        res = self.client().patch('/movies/1', json=self.patch_date, headers={'Content-Type': 'application/json', 'Authorization': 'Bearer {}'.format(castingDirectorJWT)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['movie']))

    def test_403_not_autherized_patch_movie_date(self):
        res = self.client().patch('/movies/1', json=self.patch_date, headers={'Content-Type': 'application/json', 'Authorization': 'Bearer {}'.format(castingAssistantJWT)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['code'], 'unauthorized')

    def test_delete_movie(self):
        res = self.client().delete('/movies/2', headers={'Content-Type': 'application/json', 'Authorization': 'Bearer {}'.format(executiveProducerJWT)})
        data = json.loads(res.data)

        movie = Movie.query.filter(Movie.id == 1).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], 2)
        self.assertEqual(movie, None)

    def test_404_delete_movie_doesnot_exist(self):
        res = self.client().delete('/movies/10', headers={'Content-Type': 'application/json', 'Authorization': 'Bearer {}'.format(executiveProducerJWT)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource Not Found')


    def test_delete_actor(self):
        res = self.client().delete('/actors/2', headers={'Content-Type': 'application/json', 'Authorization': 'Bearer {}'.format(executiveProducerJWT)})
        data = json.loads(res.data)

        actor = Actor.query.filter(Actor.id == 1).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], 2)
        self.assertEqual(actor, None)

    def test_404_delete_actor_doesnot_exist(self):
        res = self.client().delete('/actors/10', headers={'Content-Type': 'application/json', 'Authorization': 'Bearer {}'.format(executiveProducerJWT)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource Not Found')


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()