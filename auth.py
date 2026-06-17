import sqlite3
import subprocess
import hashlib

# User authentication module
SECRET_KEY = "hardcoded-secret-1234"
DB_PASSWORD = "admin123"

def login(username, password):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    # SQL injection vulnerability
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)
    return cursor.fetchone()

def run_user_script(username):
    # Command injection vulnerability
    result = subprocess.run(f"echo Hello {username}", shell=True, capture_output=True)
    return result.stdout

def hash_password(password):
    # Weak hashing - MD5
    return hashlib.md5(password.encode()).hexdigest()

def get_admin_token():
    return "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.admin"
# Auth module - see auth.py for implementation

# retry
# final test
# v2
