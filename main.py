from flask import Flask, render_template,request
from data import getMembers,sendApplicant
app = Flask(__name__ )

@app.route("/")
def homepage():
  group = getMembers()
  return render_template("index.html",Group = group)
@app.route("/register")
def register():
  return render_template("register.html")
  
@app.route("/registration", methods=["post"])
def info():
  d = request.form
  #sendApplicant(d)
  return render_template("submit.html")
if __name__ == "__main__":
  app.run(host="0.0.0.0",debug=True)


