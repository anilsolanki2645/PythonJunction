import mysql
import mysql.connector
mydb = mysql.connector.connect(
  database="employee",  
  host="localhost",
  user="root",
  passwd=""
)

cursor = mydb.cursor()

#cursor.execute("insert into student values('ankit',12369)")

#cursor.execute("delete from student where id=12369")

#cursor.execute("update student set name='Arun' where id=421")

#cursor.execute("select name from student where id=421")

mydb.commit()

#cursor.execute('select * from student')

cursor.execute("select name from student where id=421")

rows = cursor.fetchall()

print("total number of rows:",cursor.rowcount)

for row in rows:
  print(row)

mydb.close()
cursor.close()
