#!python.exe
import os, cgi
import base
import db
import session

params = cgi.FieldStorage()
session_id = session.get_session_id()
session_data = session.get_session_data()

if os.environ['REQUEST_METHOD'].upper() == 'POST':
    subjects = db.get_all_subjects()
    for subject in subjects:
        subject_name = subject[1]
        selected_status = params.getvalue(subject_name)
        if selected_status:
            session_data[subject_name] = selected_status
    session.add_to_session(session_data, session_id)

selected_year = params.getvalue('year')
if selected_year not in ['1', '2', '3', 'list all']:
    selected_year = '1'

def print_submit_buttons():
    for y in ['1', '2', '3']:
        print('<input type="submit" name="year" value="' + y +  '">')
    print('<input type="submit" name="year" value="list all">')

def print_table_header(title):
    print('<table border="1">')
    print('<caption>' + title + '</caption>')
    print('<tr>')
    print('<th>Subject</th>')
    print('<th>ECTS</th>')
    print('<th>Status</th>')
    print('</tr>')

def print_subject_row(name, ects, selected_status):
    print("<tr>")
    print("<td>" + name + "</td>")
    print("<td>" + str(ects) + "</td>")
    print("<td>")
    for status in ['not selected', 'enrolled', 'passed']:
        checked = 'checked' if selected_status == status else ''
        print('<label><input type="radio" name="' + name + '" value="' + status + '" ' + checked + '> ' + status + '</label><br>')
    print("</td>")
    print("</tr>")

subjects = db.get_all_subjects()

base.start_html()
print('<form method="POST">')
print_submit_buttons()

if session_data:
    print('<a href="logout.py">Logout</a><br><br>')
    print('<a href="change_password.py">Change Password</a><br><br>')


if selected_year in ['1', '2', '3']:
    print_table_header(selected_year + ". Year")
    for subject in subjects:
        if subject[3] == int(selected_year):
            name = subject[1]
            ects = subject[2]
            selected_status = session_data.get(name, 'not selected') # zasto kada maknem .get mi neradi odnosno ne ispise podatke u tablici a stoji kao da ne radi nista?? 
            print_subject_row(name, ects, selected_status)
    print("</table>")

elif selected_year == 'list all':
    print_table_header("All Subjects")
    total_ects_enrolled = 0
    for subject in subjects:
        name = subject[1]
        ects = subject[2]
        status = session_data.get(name, 'not selected')
        print("<tr>")
        print("<td>" + name + "</td>")
        print("<td>" + str(ects) + "</td>")
        print("<td>" + status + "</td>")
        print("</tr>")
        if status == 'enrolled':
            total_ects_enrolled += ects
    print("<tr><td></td><td><strong>Total Enrolled:</strong></td><td>" + str(total_ects_enrolled) + "</td></tr>")
    print("</table>")

print("</form>")
base.finish_html()
