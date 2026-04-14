from werkzeug.security import generate_password_hash, check_password_hash
from utils.db import get_db_connection

def hash_password(password):
    """Hash a password using Werkzeug"""
    return generate_password_hash(password)

def verify_password(password_hash, password):
    """Verify a password against its hash"""
    return check_password_hash(password_hash, password)

def authenticate_user(username, password):
    """Authenticate a user and return user info if valid"""
    user = get_user_by_username(username)
    if user and verify_password(user['password_hash'], password):
        return {'id': user['id'], 'username': user['username'], 'role': user['role']}
    return None

def get_user_by_username(username):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()

    conn.close()
    return user