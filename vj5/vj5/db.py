#!python.exe
import mysql.connector
import json
import password_pomoc


def get_DB_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="ducan2"  
    )
    
def get_all_subjects():
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM subjects")
    return cursor.fetchall()    

def create_user(username,email, password):
    query = "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)"
    hashed_password = password_pomoc.hash_password(password)
    values = (username, email, hashed_password)
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    try:
        cursor.execute(query, values)
        mydb.commit()
    except:
        return None
    return cursor.lastrowid 

def get_user_by_username(username):
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    query = "SELECT * FROM users where name='" + username + "'"
    cursor.execute(query)
    myresult = cursor.fetchone()
    return myresult

def create_session():
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    query = "INSERT INTO sessions (data) VALUES (%s)"
    values = (json.dumps({}),)
    cursor.execute(query, values)
    mydb.commit()
    return cursor.lastrowid

def get_session(session_id):
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM sessions WHERE session_id=" + str(session_id))
    result = cursor.fetchone()
    #print(result)
    return result[0], json.loads(result[1])
    
def replace_session(session_id, data):
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("REPLACE INTO sessions(session_id, data) VALUES (%s, %s)", (session_id, json.dumps(data)))
    mydb.commit()

def destroy_session(session_id):
    query = "DELETE FROM sessions WHERE session_id = (%s)"
    values = (session_id,)
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute(query, values)
    mydb.commit()

def get_user_by_id(user_id):
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    query = "SELECT * FROM users WHERE id = %s"
    cursor.execute(query, (user_id,))
    return cursor.fetchone()

def update_user_password(user_id, new_hashed_password):
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    query = "UPDATE users SET password = %s WHERE id = %s"
    cursor.execute(query, (new_hashed_password, user_id))
    mydb.commit()









    