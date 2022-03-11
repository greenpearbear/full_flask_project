from sqlalchemy import desc

from dao.model.movie_model import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Movie).all()

    def get_all_new_and_page(self, limit, offset, status):
        if limit > 0 and status == 'new':
            return self.session.query(Movie).order_by(desc(Movie.year)).limit(limit).offset(offset).all()
        elif limit > 0:
            return self.session.query(Movie).limit(limit).offset(offset).all()
        elif status == 'new':
            return self.session.query(Movie).order_by(desc(Movie.year)).all()

    def get_one(self, uid):
        return self.session.query(Movie).filter(Movie.id == uid).one()
