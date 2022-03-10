from sqlalchemy import desc
from helpers.constants import MOVIES_PER_PAGE

from dao.model.movie_model import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Movie).all()

    def get_all_new_and_page(self, page):
        return self.session.query(Movie).order_by(desc(Movie.id)).paginate(page, MOVIES_PER_PAGE, False).items()

    def get_all_new(self):
        return self.session.query(Movie).order_by(desc(Movie.id)).all()

    def get_all_page(self, page):
        return self.session.query(Movie).paginate(page, MOVIES_PER_PAGE, False).items()

    def get_one(self, uid):
        return self.session.query(Movie).filter(Movie.id == uid).one()
