#!python.exe

import cgi
params = cgi.FieldStorage()
Lozinka = params.getvalue("password")
Lozinkadva = params.getvalue("repeat_password")

if(Lozinka !=Lozinkadva):
  print('''
  <!DOCTYPE html>
  <html>
  <body>      
    <form action="forma1.py" method="post">
        <h3 style='color: red;'>Lozinke nisu iste! Kliknite za povratak.</h3>
        <input type="submit" value="Povratak">
    </form>
  </body>
  </html>
    ''')
else:

  print ('''
  <!DOCTYPE html>
  <html>
  <body>


  <form action="forma3.py" method="post">
    Status:<br>
    <input type="radio" name="vrsta_studija" value="izvanredni" checked> izvanredni studij<br>
    <input type="radio" name="vrsta_studija" value="redovni"> redovni studij<br>
    email:<br>
    <input type="text" name="mail" value="" required>
    <br>
    Smjer:<br>
   <select name="smjer_studija">
      <option value="programiranje">programiranje</option>
     <option value="baze_podataka">baze podataka</option>
     <option value="mreze">mreze</option>
      <option value="informacijski_sustavi">informacijski sustavi</option>
   </select>
    <br>
    <input type="checkbox" name="zavrsni" value="da"> zavrsni <br>
    <input type="submit" value="next">
    <br><br>''')
  print ('<input type="hidden" name="ime" value="' + params.getvalue("firstname") + '">')
  print ('<input type="hidden" name="lozinka" value="' + params.getvalue("password") + '">')
  print ('<input type="hidden" name="ponovi_lozinku" value="' + params.getvalue("repeat_password") + '">')

  print ('''
  <br>
  </form>

  </body>
  </html>''')


