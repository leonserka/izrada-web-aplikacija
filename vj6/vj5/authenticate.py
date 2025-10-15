#!python.exe
import password_pomoc
import db

def register(username, email, password):
    user_id = db.create_user(username,email, password)
    if user_id:
        return True
    else:
        return False

def login(username, password):
    user = db.get_user_by_username(username)
    if user and password_pomoc.verify_password(password, user[3]):
        return True, user[0]
    return False, None




