from setup_db import db
from marshmallow import Schema, fields


class Movie(db.Model):
    __table_name__ = 'movie'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=True)
    description = db.Column(db.String(255), nullable=True)
    trailer = db.Column(db.String(255), nullable=True)
    year = db.Column(db.Integer, nullable=True)
    rating = db.Column(db.Float, nullable=True)
    genre_id = db.Column(db.Integer, db.ForeignKey("genre.id"), nullable=True)
    #genre = db.relationship("Genre")
    director_id = db.Column(db.Integer, db.ForeignKey("director.id"), nullable=True)
    #director = db.relationship("Director")


class MovieSchema(Schema):
    id = fields.Int()
    title = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int()
    rating = fields.Float()
    genre_id = fields.Int()
    director_id = fields.Int()
