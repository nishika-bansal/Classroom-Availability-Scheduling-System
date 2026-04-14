from flask import Blueprint, request, jsonify
from controllers.auth_controller import login_user

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    print("login api hit")
    """Login endpoint"""
    data = request.get_json()
    print("Data Received:",data)
    response=login_user(data)
    print("sending response ",response)
    return jsonify(response)