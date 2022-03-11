import hashlib
import base64
import hmac
from dao.user_dao import UserDAO
from helpers.constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS
from flask import abort


class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_all(self):
        return self.dao.get_all()

    def get_one(self, uid):
        return self.dao.get_one(uid)

    def get_email(self, email):
        return self.dao.get_email(email)

    def post(self, data):
        data['password'] = self.generate_password(data['password'])
        return self.dao.post(data)

    def update(self, uid, data):
        user = self.get_one(uid)
        if 'name' in data:
            user.name = data.get("name")
        if 'surname' in data:
            user.surname = data.get("surname")
        if 'favourite_genre' in data:
            user.favorite_genre = data.get('favourite_genre')
        return self.dao.put(user)

    def update_password(self, uid, password_old, password_new):
        user = self.get_one(uid)
        if not self.compare_password(user.password, password_old):
            abort(401)
        password_new_hash = self.generate_password(password_new)
        user.password = password_new_hash
        return self.dao.put(user)

    def generate_password(self, password):
        hash_digest = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        )
        return base64.b64encode(hash_digest)

    def compare_password(self, password_hash, other_password):
        return hmac.compare_digest(base64.b64decode(password_hash),
                                   hashlib.pbkdf2_hmac('sha256',
                                                       other_password.encode('utf-8'),
                                                       PWD_HASH_SALT,
                                                       PWD_HASH_ITERATIONS))
