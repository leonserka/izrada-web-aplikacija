#!python.exe
import cgi
import podaci
import base
import os
from http import cookies

params = cgi.FieldStorage()


cookies_string = os.environ.get('HTTP_COOKIE', '')
all_cookies = cookies.SimpleCookie(cookies_string)
cookie = cookies.SimpleCookie()
for subject in podaci.subjects.values():
    subject_name = subject['name']
    if params.getvalue(subject_name):
        cookie[subject_name] = params.getvalue(subject_name)
print(cookie.output())
print("")


if params.getvalue('year'):
    year = params.getvalue('year')
else:
    year = 1

def print_submit_buttons():
    for k in podaci.year_ids:
        print('<input type ="submit" name="year" value="' + k + '">')
    
    print('<input type="submit" name="year" value="list all">')    

def check_year(year):
    #print(year)
    for k in podaci.year_ids:
      #print(k)
        if year == k:
            return podaci.year_ids.get(k)

base.start_html()

print("""
<form action="" method="POST">""")

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
            if params.getvalue(name):
                selected = params.getvalue(name)
            elif all_cookies.get(name):
                selected = all_cookies.get(name).value
            else:
                selected = 'not selected'
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
            if params.getvalue(name):
                selected = params.getvalue(name)
            elif all_cookies.get(name):
                selected = all_cookies.get(name).value
            else:
                selected = 'not selected'
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
            if params.getvalue(name):
                selected = params.getvalue(name)
            elif all_cookies.get(name):
                selected = all_cookies.get(name).value
            else:
                selected = 'not selected'
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
              if params.getvalue(name):
                selected = params.getvalue(name)
              elif all_cookies.get(name):
                selected = all_cookies.get(name).value
              else:
                selected = 'not selected'
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
              if params.getvalue(name):
                  selected = params.getvalue(name)
              elif all_cookies.get(name):
                  selected = all_cookies.get(name).value
              else:
                  selected = 'not selected'
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
              if params.getvalue(name):
                  selected = params.getvalue(name)
              elif all_cookies.get(name):
                  selected = all_cookies.get(name).value
              else:
                  selected = 'not selected'
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