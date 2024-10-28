from flask import Blueprint, request, jsonify
from services.userService import UserService

auth_bp = Blueprint('auth', __name__)
user_service = UserService()

@auth_bp.route('/signup', methods=['POST'])
def signup():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    if not email or not password:
        return jsonify({"message": "Email and password are required"}), 400
    user, error = user_service.signup_user(email, password)
    if error:
        return jsonify({"message": error}), 400
    return jsonify({"message": "User created successfully"}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    if not email or not password:
        return jsonify({"message": "Email and password are required"}), 400
    user, error = user_service.login_user(email, password)
    if error:
        return jsonify({"message": error}), 400
    return jsonify({"message": "Login successful", "user": user.toDict()}), 200