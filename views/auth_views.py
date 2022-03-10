from flask_restx import Resource, Namespace
from flask import request
from implemented import auth_service, user_service
from helpers.decorators import auth_required

auth_ns = Namespace('auth')


@auth_ns.route('/login')
class AuthView(Resource):
    def post(self):
        data = request.json

        email = data.get('email', None)
        password = data.get('password', None)

        if None is [email, password]:
            return "", 400

        tokens = auth_service.generate_tokens(email, password)

        return tokens, 201

    @auth_required
    def put(self):
        data = request.json
        token = data.get('refresh_token')

        tokens = auth_service.approve_refresh_token(token)

        return tokens, 201


@auth_ns.route('/register')
class Register(Resource):
    def post(self):
        data = request.json

        email = data.get('email', None)
        password = data.get('password', None)

        if None is [email, password]:
            return "", 400

        new_user = user_service.post(data)
        return "", 201, {"location": f"/users/{new_user.id}"}
