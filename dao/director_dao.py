from dao.model.director_model import Director


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, uid):
        return self.session.query(Director).filter(Director.id == uid).one()

    def get_all(self):
        return self.session.query(Director).all()

    def get_page_all(self, limit, offset):
        return self.session.query(Director).limit(limit).offset(offset).all()
