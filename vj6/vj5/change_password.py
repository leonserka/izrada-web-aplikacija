#!python.exe
import base
import os
import cgi
import db
import session
import password_pomoc

params = cgi.FieldStorage()

session_data = session.get_session_data()
user_id = session_data.get("user_id") if session_data else None

passwordCheck = True
newPasswordUpdate = True
samePassword = False

if not user_id:
    print("Location: login.py")
else:
    user = db.get_user_by_id(user_id)  

    if params.getvalue("return"):
        print('Location: index.py')

    elif os.environ["REQUEST_METHOD"].upper() == "POST":
        old_password = params.getvalue("password")
        new_password = params.getvalue("newPassword")
        new_password2 = params.getvalue("newPassword2")

        if not password_pomoc.verify_password(old_password, user[3]):
            passwordCheck = False
        elif new_password != new_password2:
            newPasswordUpdate = False
        elif old_password == new_password:
            samePassword = True
        else:
            hashed = password_pomoc.hash_password(new_password)
            db.update_user_password(user_id, hashed)
            session.destroy_session()
            print('Location: login.py')

    base.start_html()
    print(f'''
    <form method="POST">
    <table>
      <tr>
        <td>
            <h2>Promjena lozinke:</h2>
            <p> Username: {user[1]} </p>
            <input type="password" name="password" placeholder="Stara lozinka"><br><br>
            <input type="password" name="newPassword" placeholder="Nova lozinka"><br><br>
            <input type="password" name="newPassword2" placeholder="Ponovi novu lozinku"><br><br>
            <input type="submit" name="change" value="Promijeni"> <input type="submit" name="return" value="Natrag">
        </td>
      </tr>
    </table>
    </form>
    ''')

    if os.environ["REQUEST_METHOD"].upper() == "POST":
        if not passwordCheck:
            print("<p><b>ERROR:</b> Krivo unesena stara lozinka</p>")
        elif not newPasswordUpdate:
            print("<p><b>ERROR:</b> Nove lozinke se ne podudaraju</p>")
        elif samePassword:
            print("<p><b>ERROR:</b> Nova lozinka ne može biti ista kao stara</p>")

    base.finish_html()
