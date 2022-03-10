from dao.model.user_model import User


class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(User).all()

    def get_one(self, uid):
        return self.session.query(User).filter(User.id == uid).one()

    def post(self, data):
        user = User(**data)
        with self.session.begin():
            self.session.add(user)
        return user

    def put(self, user):
        with self.session.begin():
            self.session.add(user)
        return user
