from dao.movie_dao import MovieDAO


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_all(self):
        return self.dao.get_all()

    def get_all_new_page(self, page):
        return self.dao.get_all_new_and_page(page)

    def get_all_new(self):
        return self.dao.get_all_new()

    def get_all_page(self, page):
        return self.dao.get_all_page(page)

    def get_one(self, uid):
        return self.dao.get_one(uid)
