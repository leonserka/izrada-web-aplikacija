#!python.exe
import base
import session
import db
import cgi

params = cgi.FieldStorage()

data = session.get_session_data()
for key, value in data.items():
    if key == 'user_id':
        user_id = value
role = db.get_user_role(user_id)

base.start_html()

if role == "student":
    print("Nemate pravo pristupa! <br><br>")
    print('<a href="index.py">Back</a>')
else:
    students = db.get_students()
    print('<tr><th>Popis studenata</th></tr>')
    print('<br>')
    for student in students:
        id = student[0]
        name = student[1]
        print('<br>')
        print(f'<tr><td><a href="upisni_list.py?id={id}">{name}</a></td></tr>')
    print('<br><br><a href="index.py">Back</a>')

base.finish_html()
