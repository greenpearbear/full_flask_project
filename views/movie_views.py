from flask_restx import Resource, Namespace
from flask import request
from dao.model.movie_model import MovieSchema
from implemented import movie_service

movies_ns = Namespace('movies')


@movies_ns.route('/')
class MoviesView(Resource):
    def get(self):
        status = request.args.get('status')
        page = request.args.get('page')
        if status or page:
            all_movies = movie_service.get_all_new_and_page(status=status, page=page)
            return MovieSchema(many=True).dump(all_movies), 200
        all_movies = movie_service.get_all()
        return MovieSchema(many=True).dump(all_movies), 200


@movies_ns.route('/<int:uid>')
class MovieView(Resource):
    def get(self, uid: int):
        try:
            movie = movie_service.get_one(uid)
            return MovieSchema().dump(movie), 200
        except Exception as e:
            return str(e), 404
