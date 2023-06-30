from sqlalchemy import create_engine,text, insert
import os

#retrieve data from the database
def getMembers():
  db_connect_string = os.getenv("database_info")
  ssl = {
     "ca": "/etc/ssl/certs/ca-certificates.crt"
    }
  engine = create_engine(db_connect_string, connect_args={"ssl": ssl})
  
  with engine.connect() as connection:
    result = connection.execute(text("SELECT *FROM members;"))
    members = []
    for row in result.all():
        members.append(dict(row._mapping))
  return members;

#send data to the database
def sendApplicant(data):
  db_connect_string = os.getenv("database_info")
  ssl = {
     "ca": "/etc/ssl/certs/ca-certificates.crt"
    }
  engine = create_engine(db_connect_string, connect_args={"ssl": ssl})
  
  with engine.connect() as connection:
    query = text('INSERT INTO members("_name","_surname","title","email") VALUES(:n,:s,:c,:e);')
    connection.execute(query,n=data["name"],s=data["surname"],c="C",e=data["email"])
    connection.commit()
  