from flask_restx import Resource, Namespace
from flask import request, abort
from dao.model.user_model import UserSchema
from implemented import user_service
from helpers.decorators import auth_required

users_ns = Namespace('user')


@users_ns.route('/')
class UserView(Resource):
    @auth_required
    def get(self, id_user):
        try:
            user = user_service.get_one(id_user)
            return UserSchema().dump(user), 200
        except Exception as e:
            return str(e), 404

    @auth_required
    def patch(self, id_user):
        data = request.json
        try:
            user_service.update(id_user, data)
            return "", 204
        except Exception as e:
            return str(e), 404


@users_ns.route('/password')
class UserReplacePasswordView(Resource):
    @auth_required
    def put(self, id_user):
        try:
            data = request.json
            password_old = data.get('password_1', None)
            password_new = data.get('password_2', None)
            if None in [password_old, password_new]:
                abort(400)
            print(data)
            user_service.update_password(id_user, password_old, password_new)
            return "", 204
        except Exception as e:
            print(e)
            return str(e), 404
