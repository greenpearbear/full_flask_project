from dao.favorites_movies_dao import FavoritesDAO


class FavoritesService:
    def __init__(self, dao: FavoritesDAO):
        self.dao = dao

    def post(self, data):
        return self.dao.post(data)

    def delete(self, data):
        return self.dao.delete(data)
