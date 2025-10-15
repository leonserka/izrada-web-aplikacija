#!python.exe
import cgi
import db
import predmeti
import base

params = cgi.FieldStorage()

student_id = params.getvalue('id')  
user = db.get_user_by_id(student_id)
username = user[1] if user else "Unknown"

base.start_html()
print('<br><br><a href="popis.py">Back</a>')
print('<br>')
print('Upisni list studenta: <strong>' + username + '</strong>')
print('<br>')
print(''' 
    <table border="1">
    <tr>
        <th>Subject</th>
        <th>Status</th>
        <th>Ects</th>
    </tr>
''')

sum_ects = 0  
subjects = db.get_subjects()  
data2 = db.get_upisni_list()  

# print("Subjects data:")
# for subject in subjects:
#     print(subject)
    
# print("Enrollment data (upisni_list):")
# for entry in data2:
#     print(entry)

for subject in subjects:
    subject_id = subject[0]  
    subject_name = subject[1] 
    ects = subject[2] 

    for entry in data2:
        if entry[1] == int(student_id) and entry[2] == subject_id:  
            status = entry[3]  
            
            #print(f"Match found: Student ID {student_id} is {status} in {subject_name} (ECTS: {ects})")

            if status == "enr":
                sum_ects += ects

            print(f'''
                <tr>  
                    <td>{subject_name}</td> 
                    <td>{status}</td>
                    <td>{ects}</td>
                </tr>
            ''')

print(f'''
    <tr>
        <td></td>
        <td>Total (enrolled):</td>
        <td>{sum_ects}</td>
    </tr>
</table>
''')

base.finish_html()
