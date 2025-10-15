#!python.exe

import cgi
import os
import cgitb
cgitb.enable(display=0, logdir="")

print  ("""
<!DOCTYPE html>
<html>
<body>
<form action="forma2.py" method="post">
  Ime:<br>
  <input type="text" name="firstname" value="" required>
  <br>
  Lozinka:<br>
  <input type="password" name="password" value="" required>
  <br>
  Ponovi Lozinku:<br>
  <input type="password" name="repeat_password" value="" required>
  <br><br>
  
  <input type="submit" value="next">
</form> 
</body>
</html>
""")

params = cgi.FieldStorage() 

