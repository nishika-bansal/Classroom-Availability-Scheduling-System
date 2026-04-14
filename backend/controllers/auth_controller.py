from utils.db import get_user_by_username

def login_user(data):
    username = data.get("username")
    password = data.get("password")

    user = get_user_by_username(username)

    if not user:
        return {
            "status": "error",
            "message": "Invalid username or password"
        }

    return {
        "status": "success",
        "message": "login successful",
        "user": {
            "username": username,
            "role": user["role"]
        }
    }