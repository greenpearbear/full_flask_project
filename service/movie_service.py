from dao.movie_dao import MovieDAO
from helpers.constants import MOVIES_PER_PAGE


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_all(self):
        return self.dao.get_all()

    def get_all_new_and_page(self, status, page):
        limit = 0
        offset = 0
        if page:
            limit = MOVIES_PER_PAGE
            offset = (page - 1) * limit
        return self.dao.get_all_new_and_page(limit=limit, offset=offset, status=status)

    def get_one(self, uid):
        return self.dao.get_one(uid)
