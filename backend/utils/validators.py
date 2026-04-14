from datetime import datetime

def validate_login_data(data):
    """Validate login data"""
    required_fields = ['username', 'password']
    for field in required_fields:
        if field not in data or not data[field]:
            return False, f"Missing required field: {field}"
    return True, None

def validate_classroom_data(data):
    """Validate classroom data"""
    required_fields = ['room_number', 'capacity', 'type']
    for field in required_fields:
        if field not in data or not data[field]:
            return False, f"Missing required field: {field}"

    if not isinstance(data['capacity'], int) or data['capacity'] <= 0:
        return False, "Capacity must be a positive integer"

    return True, None

def validate_schedule_data(data):
    """Validate schedule data"""
    if (('room_id' not in data or not data['room_id']) and
        ('room_number' not in data or not data['room_number'])):
        return False, "Missing required field: room_id or room_number"

    required_fields = ['course', 'faculty', 'date', 'start_time', 'end_time']
    for field in required_fields:
        if field not in data or not data[field]:
            return False, f"Missing required field: {field}"

    # Validate time format
    try:
        start = datetime.strptime(data['start_time'], '%H:%M')
        end = datetime.strptime(data['end_time'], '%H:%M')
        if start >= end:
            return False, "Start time must be before end time"
    except ValueError:
        return False, "Invalid time format. Use HH:MM"

    # Validate date format
    try:
        datetime.strptime(data['date'], '%Y-%m-%d')
    except ValueError:
        return False, "Invalid date format. Use YYYY-MM-DD"

    return True, None

def validate_availability_data(data):
    """Validate availability check data"""
    if (('room_id' not in data or not data['room_id']) and
        ('room_number' not in data or not data['room_number'])):
        return False, "Missing required field: room_id or room_number"

    required_fields = ['date', 'start_time', 'end_time']
    for field in required_fields:
        if field not in data or not data[field]:
            return False, f"Missing required field: {field}"

    # Validate time format
    try:
        start = datetime.strptime(data['start_time'], '%H:%M')
        end = datetime.strptime(data['end_time'], '%H:%M')
        if start >= end:
            return False, "Start time must be before end time"
    except ValueError:
        return False, "Invalid time format. Use HH:MM"

    # Validate date format
    try:
        datetime.strptime(data['date'], '%Y-%m-%d')
    except ValueError:
        return False, "Invalid date format. Use YYYY-MM-DD"

    return True, None

def validate_login_data(data):
    """Validate login data"""
    required_fields = ['username', 'password']
    for field in required_fields:
        if field not in data or not data[field]:
            return False, f"Missing required field: {field}"
    return True, None