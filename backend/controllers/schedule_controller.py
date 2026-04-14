from utils.db import get_db_connection

# 📋 GET ALL SCHEDULES
def get_all_schedules():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT schedules.*, classrooms.room_number
        FROM schedules
        JOIN classrooms ON schedules.room_id = classrooms.id
        ORDER BY schedules.date, schedules.start_time
    """)

    schedules = cursor.fetchall()
    conn.close()

    return {
        "status": "success",
        "data": [dict(s) for s in schedules]
    }, 200


# ⚠️ CHECK CONFLICT
def check_conflict(data):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM schedules WHERE date = ?", (data['date'],))
    schedules = cursor.fetchall()

    for s in schedules:
        # Room conflict
        if s["room_id"] == data["room_id"]:
            if not (data["end_time"] <= s["start_time"] or data["start_time"] >= s["end_time"]):
                conn.close()
                return "Room already booked"

        # Faculty conflict
        if s["faculty"] == data["faculty"]:
            if not (data["end_time"] <= s["start_time"] or data["start_time"] >= s["end_time"]):
                conn.close()
                return "Faculty already busy"

    conn.close()
    return None


# ➕ ADD SCHEDULE
def add_schedule(data):
    try:
        print("Incoming data:", data)  # debug

        # ✅ TIME VALIDATION
        if data["start_time"] >= data["end_time"]:
            return {"status": "error", "message": "Invalid time"}, 400

        # ✅ CONFLICT CHECK
        conflict = check_conflict(data)
        if conflict:
            return {"status": "error", "message": conflict}, 400

        conn = get_db_connection()
        cursor = conn.cursor()

        # ✅ DIRECTLY USE room_id (NO room_number)
        cursor.execute("""
            INSERT INTO schedules (room_id, course, faculty, date, start_time, end_time)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            data["room_id"],
            data["course"],
            data["faculty"],
            data["date"],
            data["start_time"],
            data["end_time"]
        ))

        conn.commit()
        conn.close()

        return {
            "status": "success",
            "message": "Scheduled successfully"
        }, 201

    except Exception as e:
        print("ERROR:", e)
        return {
            "status": "error",
            "message": str(e)
        }, 500