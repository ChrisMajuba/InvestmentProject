import mysql.connector
import os

#retrieve data from the database
def getMembers():
  mydb = mysql.connector.connect(
  host=os.environ['host'],
  user=os.environ['user'],
  password=os.environ['password'],
    database=os.environ['database'],
    ssl_ca   = "/etc/ssl/cert.pem"
  )
  mycursor = mydb.cursor()
  mycursor.execute("SELECT* FROM members;")
  members = []
  for m in mycursor.fetchall():
   members.append(dict(zip(mycursor.column_names,m)))
  if mycursor != None:
    mycursor.close()
  if mydb != None:
    mydb.close()
  return members;

#send data to the database
def sendApplicant(data):
  mydb = mysql.connector.connect(
  host=os.environ['host'],
  user=os.environ['user'],
  password=os.environ['password'],
    database=os.environ['database']
  )
  mycursor = mydb.cursor()
  mycursor.execute("INSERT INTO members(_name,_surname,title,email) VALUES(%s,%s,%s,%s);",(data["name"],data["surname"],"C",data["email"]));
  mydb.commit()
  if mycursor != None:
    mycursor.close()
  if mydb != None:
    mydb.close()