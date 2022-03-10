from flask_restx import Resource, Namespace
from flask import request
from dao.model.user_model import UserSchema
from implemented import user_service
from helpers.decorators import auth_required

users_ns = Namespace('user')


@users_ns.route('/')
class UsersView(Resource):
    @auth_required
    def get(self):
        try:
            user = user_service.get_one(1)
            return UserSchema().dump(user), 200
        except Exception as e:
            return str(e), 404

    @auth_required
    def patch(self):
        pass


@users_ns.route('/password')
class UserView(Resource):
    @auth_required
    def put(self):
        try:
            req_json = request.json
            user = user_service.put(1, req_json)
            return UserSchema().dump(user), 200
        except Exception as e:
            return str(e), 404
