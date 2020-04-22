from flask import Flask
from flask import render_template
from flask import request
from flask import Flask, session, redirect, url_for, escape, request
import pymysql.cursors

import random
import string
def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))
app = Flask(__name__)
app.secret_key =  randomString()
@app.route("/")
def index():
    if 'username' in session:
        return redirect("/dashboard")
    return  render_template('index.jinja', title='Please login')
@app.route('/login',methods = ['POST','GET'])
def login():
    if request.method== "GET":
        return redirect("/")
    user = request.form['username']
    password= request.form['pass']
    print(user)
    print(password)
    if user=="user" and password =="password":
        session['username'] = user
        return redirect("/dashboard")
    return redirect("/")
@app.route('/dashboard')
def dashboard(): 
    if not 'username' in session and session['username'] !="user":
        return redirect("/logout")
    return  render_template('dashboard.jinja', title='hello '+ session['username'])

@app.route('/logout')
def logout(): 
    if 'username' in session:
        # remove the username from the session if it is there
        session.pop('username', None)
    return redirect("/")



# Connect to the database
connection = pymysql.connect(host='192.168.0.27',
                             user='lizard',
                             password='ashrab_shai',
                             db='PMS',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
try:
    with connection.cursor() as cursor:
        # Create a new record
        sql = "create table test1;"
        cursor.execute(sql)

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()
finally:
    connection.close()

if __name__ == "__main__":
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True,host= '0.0.0.0')