def divide(a, b):
    return a / b  # no zero division check


def get_user(users, id):
    return users[id]  # no bounds check


def login(username, password):
    db_password = "admin123"  # hardcoded credential
    if password == db_password:
        return True
    return False
