from items import *

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


def checkLogin():
    return not session or (not 'username' in session and session['username'] !="user")

app = Flask(__name__)
app.secret_key = urandom(16)


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
    return  render_template('dashboard.jinja', title='hello '+ session['username'], page='Deliverables',items=Deliverable().retreiveAll())
@app.route('/deliverables')
def deliverables(): 
    return  dashboard()
@app.route('/createDeliverable')
def createDeliverable(): 
    if checkLogin():
        return redirect("/logout")
    return  render_template('createDeliverable.jinja', page='Deliverables',deliverable=None,tasks=Task().retreiveAll())
@app.route('/DeliverablesEdit',methods = ['GET'])
def editDeliverable(): 
    if checkLogin():
        return redirect("/logout")
    id = request.args['id']
    d=Deliverable()
    d.retreive(id)
    return  render_template('createDeliverable.jinja', page='Deliverables',deliverable=d,tasks=Task().retreiveAll())
@app.route('/saveDeliverable',methods = ['POST'])
def saveDeliverable(): 
    if checkLogin():
        return redirect("/logout")
    d=Deliverable()
    if 'itemID' in request.form:
        if len(request.form['itemID']) >0:
            d.retreive(int(request.form['itemID']))
    tasks=request.form.getlist('tasks[]')
    d["title"]=request.form['itemName']
    d["description"]=request.form['description']
    d["due_date"]=request.form['due_date']
    if 'itemID' in request.form:
        if len(request.form['itemID']) >0:
            unAssociateTasks(request.form['itemID'])
            d.deleteRemote()
    d.create()
    if 'itemID' in request.form:
        if len(request.form['itemID']) >0:
            d['id']=request.form['itemID']
        else:
            d.retreiveMostRecent()
    for task in tasks:
        t=Task()
        t.retreive(int(task))
        t['deliverable_id']=d['id']
        t.deleteRemote()
        t.create()
    return redirect("/deliverables")
def unAssociateTasks(deliverableID):
    t=Task()
    associatedTasks=t.retreiveWithDeliverable(int(deliverableID))
    for task in associatedTasks:
        atask=Task()
        atask.retreive(task['id'])
        atask["deliverable_id"]=None
        atask.deleteRemote()
        atask.create()
@app.route('/DeliverablesDelete',methods = ['GET'])
def deleteDeliverable(): 
    if checkLogin():
        return redirect("/logout")
    id = request.args['id']
    unAssociateTasks(id)
    d=Deliverable()
    d.retreive(id)
    d.delete()
    return deliverables()
@app.route('/tasks')
def tasks(): 
    if checkLogin():
        return redirect("/logout")
    return  render_template('dashboard.jinja', title='hello '+ session['username'], page='Tasks',items=Task().retreiveAll())
@app.route('/createTask')
def createTask(): 
    if checkLogin():
        return redirect("/logout")
    return  render_template('createTask.jinja', page='Tasks',task=None,tasks=Task().retreiveAll())
@app.route('/TasksDelete',methods = ['GET'])
def deleteTask(): 
    if checkLogin():
        return redirect("/logout")
    id = request.args['id']
    unAssociateTasks(id)
    t=Task()
    t.retreive(id)
    t.delete()
    return tasks()
@app.route('/issues')
def issues(): 
    if checkLogin():
        return redirect("/logout")
    return  render_template('dashboard.jinja', title='hello '+ session['username'], page='Issues',items=Issue().retreiveAll())
@app.route('/actionItems')
def actionItems(): 
    if checkLogin():
        return redirect("/logout")
    return  render_template('dashboard.jinja', title='hello '+ session['username'], page='Action Items',items=ActionItem().retreiveAll())
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
    return  render_template('dashboard.jinja', title='hello '+ session['username'], page='Changes')
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
