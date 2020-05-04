# Flask
from flask import (
    Flask,
    render_template,
    session,
    redirect,
    url_for,
    escape,
    request
)

# PyMySQL
import pymysql.cursors
# Random
from os import urandom
# Configuration
from config import AppConfig

def checkLogin():
    return not session or (not 'username' in session and session['username'] !="user")

app = Flask(__name__)
app.secret_key = urandom(16)

def connect():
    # Connection instance to be used with other functions
    return pymysql.connect(host=AppConfig.DATABASE_SERVER(),
                           port=AppConfig.DATABASE_PORT(),
                           user=AppConfig.DATABASE_USER,
                           password=AppConfig.DATABASE_PASSWORD,
                           db=DATABASE_DB,
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)

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
    connection = pymysql.connect(host=app.config['DATABASE_SERVER'],
                                 port=app.config['DATABASE_PORT'],
                                 user=app.config['DATABASE_USER'],
                                 password=app.config['DATABASE_PASSWORD'],
                                 db=app.config['DATABASE_DB'],
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            # Create a new record
            sql = "SHOW TABLES;"
            cursor.execute(sql)
            result = cursor.fetchone()
            print(result)
            return str(result)
        # connection is not autocommit by default. So you must commit to save
        # your changes.
        # connection.commit()
    except Error as e:
        print(e)
        return e
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
    app.config.from_object(AppConfig())
    app.run(host= '0.0.0.0')
