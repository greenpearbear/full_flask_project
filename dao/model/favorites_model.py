from setup_db import db
from marshmallow import Schema, fields


class Favorites(db.Model):
    __table_name__ = 'favorites'
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'), primary_key=True)


class UserSchema(Schema):
    user_id = fields.Int()
    movie_id = fields.Int()
