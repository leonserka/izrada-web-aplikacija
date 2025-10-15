#!python.exe
import cgi
import os
import mysql.connector
import json
from http import cookies
import podaci
import base


def get_DB_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="ducan2"  
    )

def create_session():
    query = "INSERT INTO sessions (data) VALUES (%s)"
    values = (json.dumps({}),)
    mydb = get_DB_connection()
    cursor = mydb.cursor()
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

def get_or_create_session_id():
    http_cookies_str = os.environ.get('HTTP_COOKIE', '')
    get_all_cookies_object = cookies.SimpleCookie(http_cookies_str)
    session_id = get_all_cookies_object.get("session_id").value if get_all_cookies_object.get("session_id") else None
    if session_id is None:
        session_id = create_session()
        cookies_object = cookies.SimpleCookie()
        cookies_object["session_id"] = session_id
        print(cookies_object.output())  
    return session_id


params = cgi.FieldStorage()
session_id = get_or_create_session_id()
_, session_data = get_session(session_id)


for subject in podaci.subjects.values():
    subject_name = subject["name"]
    if params.getvalue(subject_name):
        session_data[subject_name] = params.getvalue(subject_name)

replace_session(session_id, session_data)

if params.getvalue('year'):
    year = params.getvalue('year')
else:
    year = 1

def print_submit_buttons():
    for k in podaci.year_ids:
        print('<input type="submit" name="year" value="' + k + '">')
        
        
    print('<input type="submit" name="year" value="list all">')

def check_year(year):
    #print(year)
    for k in podaci.year_ids:
      #print(k)
        if year == k:
            return podaci.year_ids.get(k)

base.start_html()
print("""
<form action="" method="POST">
""")

print_submit_buttons()


if check_year(year) == 1 or year == 1:
    print("""
    <table style="width:50%">
      <tr>
        <th>1st Year</th>
        <th>Ects</th>
        <th>Status</th>
      </tr>
    """)
    for subject in podaci.subjects.values():
        if subject['year'] == 1:
            name = subject['name']
            ects = subject['ects']
            selected = session_data.get(name, 'not selected')
            print("<tr>")
            print("<td>" + name + "</td>")
            print("<td>" + str(ects) + "</td>")
            print("<td>")
            print('<input type="radio" name="' + name + '" value="not selected" ' + ('checked' if selected == 'not selected' else '') + '> Not Selected <br>')  
            print('<input type="radio" name="' + name + '" value="enrolled" ' + ('checked' if selected == 'enrolled' else '') + '> Enrolled <br>')  
            print('<input type="radio" name="' + name + '" value="passed" ' + ('checked' if selected == 'passed' else '') + '> Passed  <br>')  
            print("</td>")
            print("</tr>")
    print("</table>")

elif check_year(year) == 2:
    print("""
    <table style="width:50%">
      <tr>
        <th>2nd Year</th>
        <th>Ects</th>
        <th>Status</th>
      </tr>
    """)
    for subject in podaci.subjects.values():
        if subject['year'] == 2:
            name = subject['name']
            ects = subject['ects']
            selected = session_data.get(name, 'not selected')
            print("<tr>")
            print("<td>" + name + "</td>")
            print("<td>" + str(ects) + "</td>")
            print("<td>")
            print('<input type="radio" name="' + name + '" value="not selected" ' + ('checked' if selected == 'not selected' else '') + '> Not Selected <br>')  
            print('<input type="radio" name="' + name + '" value="enrolled" ' + ('checked' if selected == 'enrolled' else '') + '> Enrolled <br>')  
            print('<input type="radio" name="' + name + '" value="passed" ' + ('checked' if selected == 'passed' else '') + '> Passed  <br>')  
            print("</td>")
            print("</tr>")
    print("</table>")

elif check_year(year) == 3:
    print("""
    <table style="width:50%">
      <tr>
        <th>3rd Year</th>
        <th>Ects</th>
        <th>Status</th>
      </tr>
    """)
    for subject in podaci.subjects.values():
        if subject['year'] == 3:
            name = subject['name']
            ects = subject['ects']
            selected = session_data.get(name, 'not selected')
            print("<tr>")
            print("<td>" + name + "</td>")
            print("<td>" + str(ects) + "</td>")
            print("<td>")
            print('<input type="radio" name="' + name + '" value="not selected" ' + ('checked' if selected == 'not selected' else '') + '> Not Selected <br>')  
            print('<input type="radio" name="' + name + '" value="enrolled" ' + ('checked' if selected == 'enrolled' else '') + '> Enrolled <br>')  
            print('<input type="radio" name="' + name + '" value="passed" ' + ('checked' if selected == 'passed' else '') + '> Passed  <br>')  
            print("</td>")
            print("</tr>")
    print("</table>")

elif params.getvalue('year') == "list all": 
    print("""
    <table style="width:50%">
      <tr>
        <th>Predmeti</th>
        <th>Ects</th>
        <th>Status</th>
      </tr>
    """)
    
    total_ects_enrolled = 0
    
    for subject in podaci.subjects.values():  
          if subject['year'] == 1:
              name = subject['name']
              ects = subject['ects']
              selected = session_data.get(name, 'not selected')
              print("<tr>")
              print("<td>" + name + "</td>")
              print("<td>" + str(ects) + "</td>")
              print("<td>")
              print(selected.capitalize())
              
              if selected == 'enrolled':
                total_ects_enrolled += ects
              #print(total_ects_enrolled)  
              
              print("</td>")
              print("</tr>")
          if subject['year'] == 2:
              name = subject['name']
              ects = subject['ects']
              selected = session_data.get(name, 'not selected')
              print("<tr>")
              print("<td>" + name + "</td>")
              print("<td>" + str(ects) + "</td>")
              print("<td>")
              print(selected.capitalize())
              
              if selected == 'enrolled':
                total_ects_enrolled += ects
              #print(total_ects_enrolled) 
                
              print("</td>")
              print("</tr>") 
          if subject['year'] == 3:
              name = subject['name']
              ects = subject['ects']
              selected = session_data.get(name, 'not selected')
              print("<tr>")
              print("<td>" + name + "</td>")
              print("<td>" + str(ects) + "</td>")
              print("<td>")
              print(selected.capitalize())
              
              if selected == 'enrolled':
                total_ects_enrolled += ects
                #print(total_ects_enrolled) 
                
              print("</td>")
              print("</tr>")
          
          
    print("<tr>")
    print("<td>" "</td>")
    print("<td>" + "Ukupno upisano:" + "</td>")
    print("<td>")
    if total_ects_enrolled > 0:  
        print(total_ects_enrolled)
        print()
        print("</td>")
        print("</tr>")    
        print("</table>")


print('</form>')
base.end_html()


#print(params)
#print(year)
#year = check_year(params.getvalue("year"))
#print(year)