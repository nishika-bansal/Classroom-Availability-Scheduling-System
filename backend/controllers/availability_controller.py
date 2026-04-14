from utils.db import get_db_connection


from utils.db import get_db_connection

def check_availability(data):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        room_id = data.get("room_id")
        date = data.get("date")
        start_time = data.get("start_time")
        end_time = data.get("end_time")

        # ✅ VALIDATION
        if not room_id or not date or not start_time or not end_time:
            return {
                "status": "error",
                "message": "Missing required fields"
            }, 400

        # ✅ GET SCHEDULES FOR THIS ROOM + DATE
        cursor.execute("""
            SELECT * FROM schedules
            WHERE room_id = ? AND date = ?
        """, (room_id, date))

        schedules = cursor.fetchall()

        # ✅ CHECK CONFLICT
        for s in schedules:
            if not (
                end_time <= s["start_time"] or
                start_time >= s["end_time"]
            ):
                conn.close()
                return {
                    "status": "error",
                    "message": "Room is NOT available ❌"
                }, 200

        conn.close()

        # ✅ NO CONFLICT
        return {
            "status": "success",
            "message": "Room is available ✅"
        }, 200

    except Exception as e:
        print("ERROR:", e)
        return {
            "status": "error",
            "message": str(e)
        }, 500