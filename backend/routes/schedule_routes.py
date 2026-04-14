from flask import Blueprint, request, jsonify
from controllers.schedule_controller import add_schedule, get_all_schedules

schedule_bp = Blueprint('schedule', __name__)

# ➕ ADD SCHEDULE
@schedule_bp.route('/schedule', methods=['POST'])
def create_schedule_route():   # ✅ renamed (important)

    data = request.get_json()
    print("Data received:", data)   # debug

    response, status_code = add_schedule(data)

    return jsonify(response), status_code


# 📋 GET ALL SCHEDULES
@schedule_bp.route('/get-schedule', methods=['GET'])
def get_schedule():

    response, status_code = get_all_schedules()

    return jsonify(response), status_code