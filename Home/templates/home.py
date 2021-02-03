#!C:/Users/Gaurav Mori/AppData/Local/Microsoft/WindowsApps/python.exe
print("Content-type: text/html")
print()
import cgi


form =cgi.FieldStorage()
name1=str(form.getvalue('name'))
passw=str(form.getvalue('password'))

if name1=="user1" and passw=="user1":
    print ("welcome ",name1)
else:
    print("Enter valid username and password")