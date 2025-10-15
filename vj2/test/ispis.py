#!python.exe

import cgi
params = cgi.FieldStorage()

print ('''
<!DOCTYPE html>
<html>
<body>


<form action="forma1.py" method="post">
  <br><br>''')
print('')
print("Ime:",params.getvalue('ime'))
print("<br>")
print ("e-mail:",params.getvalue('mail'))
print("<br>")
print ("status:",params.getvalue('studij'))
print("<br>")
print ("smjer:",params.getvalue('smjer'))
print("<br>")
print ("zavrsni rad:",params.getvalue('zavrsni'))
print("<br>")
print ("napomene:",params.getvalue('napomene'))


print ('''
<br>
<input type="submit" value="return to start">
</form>
</body>
</html>''')