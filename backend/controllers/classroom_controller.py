from utils.db import get_db_connection
import sqlite3


# 📋 GET ALL CLASSROOMS
def get_all_classrooms():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM classrooms ORDER BY room_number")
        rooms = cursor.fetchall()

        conn.close()

        return {
            "status": "success",
            "data": [dict(r) for r in rooms]
        }, 200

    except Exception as e:
        return {
            "status": "error",
            "message": "Failed to fetch classrooms"
        }, 500


# ➕ ADD CLASSROOM
def add_classroom(data):
    try:
        room_number = data.get("room_number")
        capacity = data.get("capacity")
        room_type = data.get("type")

        # ✅ VALIDATION
        if not room_number or not capacity:
            return {
                "status": "error",
                "message": "Room number and capacity are required"
            }, 400

        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO classrooms (room_number, capacity, type)
            VALUES (?, ?, ?)
        """, (room_number, capacity, room_type))

        conn.commit()
        conn.close()

        return {
            "status": "success",
            "message": "Classroom added successfully"
        }, 201

    except sqlite3.IntegrityError:
        # ✅ HANDLE UNIQUE ERROR CLEANLY
        return {
            "status": "error",
            "message": "Room already exists ❌"
        }, 400

    except Exception as e:
        return {
            "status": "error",
            "message": "Failed to add classroom"
        }, 500


# ❌ DELETE CLASSROOM
def delete_classroom(room_id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM classrooms WHERE id = ?", (room_id,))
        conn.commit()

        if cursor.rowcount == 0:
            conn.close()
            return {
                "status": "error",
                "message": "Room not found"
            }, 404

        conn.close()
        return {
            "status": "success",
            "message": "Deleted successfully"
        }, 200

    except Exception as e:
        return {
            "status": "error",
            "message": "Failed to delete classroom"
        }, 500


# ✏️ UPDATE CLASSROOM
def update_classroom(room_id, data):
    try:
        room_number = data.get("room_number")
        capacity = data.get("capacity")
        room_type = data.get("type")

        # ✅ VALIDATION
        if not room_number or not capacity:
            return {
                "status": "error",
                "message": "Room number and capacity are required"
            }, 400

        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE classrooms
            SET room_number = ?, capacity = ?, type = ?
            WHERE id = ?
        """, (room_number, capacity, room_type, room_id))

        conn.commit()

        if cursor.rowcount == 0:
            conn.close()
            return {
                "status": "error",
                "message": "Room not found"
            }, 404

        conn.close()
        return {
            "status": "success",
            "message": "Updated successfully"
        }, 200

    except sqlite3.IntegrityError:
        return {
            "status": "error",
            "message": "Room number already exists ❌"
        }, 400

    except Exception as e:
        return {
            "status": "error",
            "message": "Failed to update classroom"
        }, 500