import os
from sqlalchemy import Column, String, Integer, Text, Date, create_engine
from flask_sqlalchemy import SQLAlchemy
import json

database_name = "castingagencydb"
database_path = "postgresql://{}:{}@{}/{}".format(
    'postgres', 'postgres', 'localhost:5432', database_name)
db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()
    # db_drop_and_create_all()


'''
db_drop_and_create_all()
    drops the database tables and starts fresh used to initialize a clean database
'''


def db_drop_and_create_all():
    db.drop_all()
    db.create_all()


'''
Association actors_movies

'''
# actors_movies = db.Table('actors_movies',
# 	db.Column('actor_id', db.Integer, db.ForeignKey('actors.id'), primary_key=True),
# 	db.Column('movie_id', db.Integer, db.ForeignKey('movies.id'), primary_key=True)
# 	)

'''
Movie

'''


class Movie(db.Model):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    release_date = Column(Date)

    def __init__(self, title, release_date):
        self.title = title
        self.release_date = release_date

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'release_date': self.release_date
        }


'''
Actor

'''


class Actor(db.Model):
    __tablename__ = 'actors'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    gender = Column(String)
    # movies = db.relationship('Movie', secondary=actors_movies, backref=db.backref('actors', lazy=True))

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender
        }
