from dao.model.favorites_model import Favorites


class FavoritesDAO:
    def __init__(self, session):
        self.session = session

    def post(self, data):
        favorites = Favorites(**data)
        with self.session.begin():
            self.session.add(favorites)
        return favorites

    def delete(self, data):
        favorites = self.session.query(Favorites).filter(Favorites.user_id == data.get('id_user'),
                                                         Favorites.movie_id == data.get('id_movie'))
        self.session.delete(favorites)
        self.session.commit()
        return "", 204
