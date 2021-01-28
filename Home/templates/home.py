#!C:/Users/Gaurav Mori/AppData/Local/Microsoft/WindowsApps/python.exe
import cgi
print("Content-type: text/html")
print()


form =cgi.FieldStorage()
name1=str(form.getvalue('name'))
passw=str(form.getvalue('password'))

if name1=="user1" and passw=="user1":
    print ("welcome ",name1)
else:
    print("Enter valid username and password")