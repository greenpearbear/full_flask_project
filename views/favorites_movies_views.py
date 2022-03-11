from flask_restx import Resource, Namespace
from implemented import favorites_service
from helpers.decorators import auth_required


favorites_movies_ns = Namespace('/favorites/movies')


@favorites_movies_ns.route('/<int:uid_movie>')
class FavoriteMovies(Resource):
    @auth_required
    def post(self, id_user, uid_movie):
        data = {
            'id_user': id_user,
            'uid_movie': uid_movie
        }
        favorites_service.post(data)
        return "", 201

    @auth_required
    def delete(self, id_user, uid_movie):
        data = {
            'id_user': id_user,
            'uid_movie': uid_movie
        }
        favorites_service.delete(data)
