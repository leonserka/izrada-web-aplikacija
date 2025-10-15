#!python.exe

import os, cgi
import base, authenticate, session

params = cgi.FieldStorage()

if os.environ['REQUEST_METHOD'].upper() == "POST":
    username = params.getvalue('username')
    password = params.getvalue('password')
    success, user_id = authenticate.login(username, password)
    if success:
        session_id = session.create_session()
        session.add_to_session({"user_id":user_id}, session_id)
        print('Location:index.py')
   


base.start_html()
print ('''<form method="POST">
username <input type="text" name="username" />
password <input type="password" name="password"/>
<input type="submit" value="Login"/>
</form>''')
base.finish_html()

