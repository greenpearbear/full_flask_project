from dao.model.genre_model import Genre


class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, uid):
        return self.session.query(Genre).filter(Genre.id == uid).one()

    def get_all(self):
        return self.session.query(Genre).all()

    def get_page_all(self, limit, offset):
        return self.session.query(Genre).limit(limit).offset(offset).all()