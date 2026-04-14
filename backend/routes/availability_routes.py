from flask import Blueprint, request, jsonify
from controllers.availability_controller import check_availability

availability_bp = Blueprint('availability', __name__)

@availability_bp.route('/check', methods=['POST', 'OPTIONS'])
def check():
    if request.method == 'OPTIONS':
        return jsonify({"status": "ok"}), 200   # ✅ handle preflight
    """Check availability endpoint"""
    data = request.get_json()
    print("Avaiability check :",data)
    response, status_code = check_availability(data)
    return jsonify(response), status_code