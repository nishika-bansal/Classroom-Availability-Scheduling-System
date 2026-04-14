from flask import Blueprint, request, jsonify
from controllers.classroom_controller import *

classroom_bp = Blueprint('classroom', __name__)

@classroom_bp.route('/add-room', methods=['POST'])
def add_room():
    """Add classroom endpoint"""
    data = request.get_json()
    response, status_code = add_classroom(data)
    return jsonify(response), status_code

@classroom_bp.route('/get-rooms', methods=['GET'])
def get_rooms():
    """Get all classrooms endpoint"""
    response, status_code = get_all_classrooms()
    return jsonify(response), status_code

@classroom_bp.route('/delete-room/<int:room_id>', methods=['DELETE'])
def delete_room(room_id):
    """Delete classroom endpoint"""
    response, status_code = delete_classroom(room_id)
    return jsonify(response), status_code

@classroom_bp.route('/update-room/<int:room_id>', methods=['PUT'])
def update_room(room_id):
    """Update classroom endpoint"""
    data = request.get_json()
    response, status_code = update_classroom(room_id, data)
    return jsonify(response), status_code