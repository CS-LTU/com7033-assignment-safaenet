# from flask import Blueprint, request, jsonify
# from services.userService import UserService

# auth_bp = Blueprint('auth', __name__)
# user_service = UserService()

# @auth_bp.route('/signup', methods=['POST'])
# def signup():
#     data = request.json
#     email = data.get('email')
#     password = data.get('password')
#     if not email or not password:
#         return jsonify({"message": "Email and password are required"}), 400
#     user, error = user_service.signup_user(email, password)
#     if error:
#         return jsonify({"message": error}), 400
#     return jsonify({"message": "User created successfully"}), 201

# @auth_bp.route('/login', methods=['POST'])
# def login():
#     data = request.json
#     email = data.get('email')
#     password = data.get('password')
#     if not email or not password:
#         return jsonify({"message": "Email and password are required"}), 400
#     user, error = user_service.login_user(email, password)
#     if error:
#         return jsonify({"message": error}), 400
#     return jsonify({"message": "Login successful", "user": user.toDict()}), 200

from flask import abort, request, jsonify, session
import flask
from flask_cors import cross_origin
from flask_restful import Resource

from services.userService import authenticate_user, register_user, update_password_service

class AuthAPI(Resource):
    def post(self):
        action = request.args.get('action')
        data = request.get_json()
        if action == 'signin':
            email = data.get("email")
            password = data.get("password")
            print(email, password)
            auth = authenticate_user(email, password)
            if auth == "UserNotFound":
                return abort(404, "User Not Found")
            if auth:
                session["user"] = email
                response = flask.jsonify({"message": "Signed in successfully", "user": email})
                response.headers.add('Access-Control-Allow-Origin', '*')
                return response
                # return jsonify({"message": "Signed in successfully", "user": email})
            return abort(400, "Invalid credentials")

        elif action == 'signup':
            email = data.get("email")
            password = data.get("password")
            if register_user(email, password):
                return jsonify({"message": "Account created successfully"})
            return abort(400, "Email already exists")

        elif action == 'update_password':
            if "user" not in session:
                return abort(401, "Unauthorized")
            old_password = data.get("old_password")
            new_password = data.get("new_password")
            if update_password_service(session["user"], old_password, new_password):
                return jsonify({"message": "Password updated successfully"})
            return abort(400, "Old password is incorrect")

        return abort(400, "Invalid action")

    def delete(self):
        session.pop("user", None)
        return jsonify({"message": "Logged out successfully"})
    

class SessionCheckAPI(Resource):
    def get(self):
        if "user" in session:
            print("LOGGED IN")
            return jsonify({"loggedIn": True, "user": session["user"]})
        else:
            print("LOGGED OUT")
        return jsonify({"loggedIn": False})