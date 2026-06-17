import subprocess
import sqlite3


def run_command(user_input):
    # command injection vulnerability
    result = subprocess.run(f"echo {user_input}", shell=True, capture_output=True)
    return result.stdout


def get_user_data(user_id):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    # SQL injection vulnerability
    query = f"SELECT * FROM users WHERE id = {user_id}"
    cursor.execute(query)
    return cursor.fetchone()


API_KEY = "sk-1234567890abcdef"  # hardcoded API key
SECRET_TOKEN = "super_secret_token_abc"
