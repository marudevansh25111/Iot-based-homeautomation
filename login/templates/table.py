import mysql.connector

#establishing the connection
conn = mysql.connector.connect(
   user='root', password='', host='localhost', database='project')

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

# Preparing SQL query to INSERT a record into the database.
sql = """INSERT INTO UserInfo    VALUES ('Mac', 'Mohan','Mohan', 9999, 'sjcb')"""

try:
   # Executing the SQL command
   cursor.execute(sql)

   # Commit your changes in the database
   conn.commit()

except:
   # Rolling back in case of error
   conn.rollback()

# Closing the connection
conn.close()