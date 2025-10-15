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
    
def create_user(username,email, password):
    query = "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)"
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
    query = "SELECT * FROM users where username='" + username + "'"
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
    query = "SELECT * FROM users WHERE user_id = %s"
    cursor.execute(query, (user_id,))
    return cursor.fetchone()

def update_user_password(user_id, new_hashed_password):
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    query = "UPDATE users SET password = %s WHERE user_id = %s"
    cursor.execute(query, (new_hashed_password, user_id))
    mydb.commit()


def update_upisni_list(student_id, subject_id, status):
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    query = """
        REPLACE INTO upisni_list (id_studenta, id_predmeta, status)
        VALUES (%s, %s, %s)
    """
    values = (student_id, subject_id, status)
    cursor.execute(query, values)
    mydb.commit()


def add_upisni_list(student_id, predmet_id, status):
    query = '''
    INSERT INTO upisni_list (id_studenta, id_predmeta, status)
    VALUES (%s, %s, %s)
    ON DUPLICATE KEY UPDATE
        status = VALUES(status);
    '''
    values = (student_id, predmet_id, status)
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    try:
        cursor.execute(query, values)
        mydb.commit()
    except:
        return None
    return cursor.lastrowid

def get_students():
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM users WHERE uloga='student'")
    myresult = cursor.fetchall()
    return myresult 

def get_user_role(user_id):
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("SELECT uloga FROM users WHERE user_id='" + str(user_id) + "'")
    myresult = cursor.fetchone()
    return myresult[0]

def get_subjects():
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    query = "SELECT * FROM subjects"
    cursor.execute(query)
    return cursor.fetchall()

def get_user_by_id_studenta(id_studenta): 
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    query = """
        SELECT subjects.name, subjects.ects, upisni_list.status
        FROM upisni_list
        JOIN subjects ON upisni_list.id_predmeta = subjects.id
        WHERE upisni_list.id_studenta = %s
    """
    cursor.execute(query, (id_studenta,))
    result = cursor.fetchall()
    
    return result

def get_upisni_list():
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    query = "SELECT * FROM upisni_list"
    cursor.execute(query)
    return cursor.fetchall()
