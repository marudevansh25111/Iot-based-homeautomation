#!C:/Users/Gaurav Mori/AppData/Local/Microsoft/WindowsApps/python.exe
import cgi
print("Content-type: text/html")
print()


form =cgi.FieldStorage()
name1=str(form.getvalue('name'))
passw=str(form.getvalue('password'))
opt=str(form.getvalue('iot'))

if name1=="user1" and passw=="user1":
    
     print('<html>')
     print('  <head> ')
   
     print('    <meta http-equiv="refresh" content="0;url=http://169.254.81.214:1880/ui/#!/0?socketid=NiUOP-obSz3agwMRAAAE" />') 
     print("  <link rel = 'icon' href = 'img/pi.png' type = 'image/x-icon'> ")
     print(' <title>IOT Home Automation</title> </head>')
     print('</html>')
else:
      print(' <title>IOT Home Automation</title> </head>')
      print("  <link rel = 'icon' href = 'img/pi.png' type = 'image/x-icon'> ")
      print("Enter valid username and password")