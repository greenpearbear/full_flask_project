from dao.director_dao import DirectorDAO
from helpers.constants import MOVIES_PER_PAGE


class DirectorService:
    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def get_all(self):
        return self.dao.get_all()

    def get_one(self, uid):
        return self.dao.get_one(uid)

    def get_page_all(self, page):
        limit = MOVIES_PER_PAGE
        offset = (page - 1) * limit
        return self.dao.get_page_all(limit=limit, offset=offset)
