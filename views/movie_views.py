from flask_restx import Resource, Namespace
from flask import request
from dao.model.movie_model import MovieSchema
from implemented import movie_service
from helpers.decorators import admin_required

movies_ns = Namespace('movies')


@movies_ns.route('/')
class MoviesView(Resource):
    def get(self):
        status = request.args.get('status')
        page = request.args.get('page', 1, type=int)
        if status and page:
            all_movies = movie_service.get_all_new_and_page(page)
            return MovieSchema(many=True).dump(all_movies), 200
        if status:
            all_movies = movie_service.get_all_new()
            return MovieSchema(many=True).dump(all_movies), 200
        if page:
            all_movies = movie_service.get_all_page(page)
            return MovieSchema(many=True).dump(all_movies), 200
        all_movies = movie_service.get_all()
        return MovieSchema(many=True).dump(all_movies), 200

    @admin_required
    def post(self):
        req_json = request.json
        new_movie = movie_service.post(req_json)
        return "", 201, {"location": f"/movies/{new_movie.id}"}


@movies_ns.route('/<int:uid>')
class MovieView(Resource):
    def get(self, uid: int):
        try:
            movie = movie_service.get_one(uid)
            return MovieSchema().dump(movie), 200
        except Exception as e:
            return str(e), 404

    @admin_required
    def put(self, uid: int):
        try:
            req_json = request.json
            movie = movie_service.put(uid, req_json)
            return MovieSchema().dump(movie), 200
        except Exception as e:
            return str(e), 404

    @admin_required
    def delete(self, uid: int):
        try:
            movie_service.delete(uid)
            return "", 204
        except Exception as e:
            return str(e), 404
