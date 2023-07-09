from sqlalchemy import create_engine,text
import os

db_connect_string = os.getenv("database_info")
engine = create_engine(db_connect_string,connect_args={
        "ssl" :{
    "ssl_ca": "/etc/ssl/cert.pem"}
    })

#retrieve data from the database
def getMembers():
  with engine.connect() as connection:
    result = connection.execute(text("SELECT *FROM members;"))
    members = []
    for row in result.all():
        members.append(dict(row._mapping))
  return members;

#send data to the database
def sendApplicant(data):
  with engine.connect() as conn:
    conn.execute(
        text("INSERT INTO members (_name, _surname,title,email) VALUES (:n,:s,:c,:e)"),[{"n": data["name"], "s": data["surname"],"c":"C","e":data["email"]}])
    conn.commit()
  