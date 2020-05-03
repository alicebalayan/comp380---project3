from flask import Flask
from flask import render_template
from flask import request
from flask import Flask, session, redirect, url_for, escape, request
import pymysql.cursors

import random
import string
def checkLogin():
    if not session or (not 'username' in session and session['username'] !="user"):
        return True
    return False
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
    if checkLogin():
        return redirect("/logout")
    return  render_template('dashboard.jinja', title='hello '+ session['username'], page='Deliverables')
@app.route('/deliverables')
def deliverables(): 
    return  dashboard()
@app.route('/createDeliverable')
def createDeliverable(): 
    if checkLogin():
        return redirect("/logout")
    return  render_template('createDeliverable.jinja')
@app.route('/tasks')
def tasks(): 
    if checkLogin():
        return redirect("/logout")
    return  render_template('dashboard.jinja', title='hello '+ session['username'], page='Tasks')
@app.route('/issues')
def issues(): 
    if checkLogin():
        return redirect("/logout")
    return  render_template('dashboard.jinja', title='hello '+ session['username'], page='Issues')
@app.route('/actionItems')
def actionItems(): 
    if checkLogin():
        return redirect("/logout")
    return  render_template('dashboard.jinja', title='hello '+ session['username'], page='Action Items')
@app.route('/decisions')
def decisions(): 
    if checkLogin():
        return redirect("/logout")
    return  render_template('dashboard.jinja', title='hello '+ session['username'], page='Decisions')
@app.route('/resources')
def resources(): 
    if checkLogin():
        return redirect("/logout")
    return  render_template('dashboard.jinja', title='hello '+ session['username'], page='Resources')
@app.route('/risks')
def risks(): 
    if checkLogin():
        return redirect("/logout")
    return  render_template('dashboard.jinja', title='hello '+ session['username'], page='Risks')
@app.route('/requirments')
def requirments(): 
    if checkLogin():
        return redirect("/logout")
    return  render_template('dashboard.jinja', title='hello '+ session['username'], page='Requirments')
@app.route('/changes')
def changes(): 
    if checkLogin():
        return redirect("/logout")
    return  render_template('dashboard.jinja', title='hello '+ session['username'], page='changes')
@app.route('/referenceDocuments')
def referenceDocuments(): 
    if checkLogin():
        return redirect("/logout")
    return  render_template('dashboard.jinja', title='hello '+ session['username'], page='Reference Documents')
@app.route('/components')
def components(): 
    if checkLogin():
        return redirect("/logout")
    return  render_template('dashboard.jinja', title='hello '+ session['username'], page='Components')
@app.route('/defects')
def defects(): 
    if checkLogin():
        return redirect("/logout")
    return  render_template('dashboard.jinja', title='hello '+ session['username'], page='Defects')
@app.route('/settings')
def settings(): 
    if checkLogin():
        return redirect("/logout")
    return  "working on it"
@app.route('/testSQL')
def mySQL():
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
            sql = "SHOW TABLES;"
            cursor.execute(sql)
            result = cursor.fetchone()
            print(result)
            return result

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        # connection.commit()

    finally:
        connection.close()
    
@app.route('/logout')
def logout(): 
    if 'username' in session:
        # remove the username from the session if it is there
        session.pop('username', None)
    return redirect("/")





if __name__ == "__main__":
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True,host= '0.0.0.0')
    