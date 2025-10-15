#!python.exe

import cgi
params = cgi.FieldStorage()
zavrsni = params.getvalue("zavrsni")

print ('''
<!DOCTYPE html>
<html>
<body>


 <form action="ispis.py" method="post">
 <br><br>
 Napomene:
 <textarea name="napomene" rows="10" cols="30">
 upisite nesto...
 </textarea> 
  <input type="submit" value="next">
  <br><br>''')
print ('<input type="hidden" name="ime" value="' + params.getvalue("ime") + '">')
print ('<input type="hidden" name="lozinka" value="' + params.getvalue("lozinka") + '">')
print ('<input type="hidden" name="ponovi_lozinku" value="' + params.getvalue("ponovi_lozinku") + '">')
print ('<input type="hidden" name="studij" value="' + params.getvalue("vrsta_studija") + '">')
print ('<input type="hidden" name="mail" value="' + params.getvalue("mail") + '">')
print ('<input type="hidden" name="smjer" value="' + params.getvalue("smjer_studija") + '">')

if zavrsni is None:
  print ('<input type="hidden" name="zavrsni" value="ne' + '">')
else:
  print ('<input type="hidden" name="zavrsni" value="' + zavrsni + '">')

print ('''
</form>
</body>
</html>''')
# print (params.getvalue('vrsta_studija'))
# print (params.getvalue('mail'))
# print (params.getvalue('smjer_studija'))
# print (params.getvalue('zavrsni'))
