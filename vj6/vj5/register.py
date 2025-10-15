#!python.exe
import os
import cgi
import base
import authenticate

params = cgi.FieldStorage()

if os.environ['REQUEST_METHOD'].upper() == "POST":
    username = params.getvalue('username')
    email = params.getvalue('email')
    password = params.getvalue('password')
    repeat_password = params.getvalue('repeat_password')

    if password != repeat_password:
        print()
        print("<h1>lozinke se ne podudara!</h1>")
        base.start_html()
        print('<a href="register.py">Go back</a>')
        base.finish_html()
    else:
        success = authenticate.register(username, email, password)
        if success:
            print("Location: login.py")
        else:
            print("Content-Type: text/html")
            print()
            print("<h1>Email se vec koristi.</h1>")
            base.start_html()
            print('<a href="register.py">Go back</a>')
            base.finish_html()

base.start_html()
print('''<form method="POST">
    Username: <input type="text" name="username" required/><br/>
    Email: <input type="email" name="email" required/><br/>
    Password: <input type="password" name="password" required/><br/>
    Repeat Password: <input type="password" name="repeat_password" required/><br/>
    <input type="submit" value="Register"/>
</form>''')
base.finish_html()

