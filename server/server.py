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
    return  render_template('createDeliverable.jinja', page='Deliverables',deliverable=None,tasks=Task().retreiveAll(),requirments=Requirment().retreiveAll())
@app.route('/DeliverablesEdit',methods = ['GET'])
def editDeliverable(): 
    if checkLogin():
        return redirect("/logout")
    id = request.args['id']
    d=Deliverable()
    d.retreive(id)
    return  render_template('createDeliverable.jinja', page='Deliverables',deliverable=d,tasks=Task().retreiveAll(),requirments=Requirment().retreiveAll())
@app.route('/saveDeliverable',methods = ['POST'])
def saveDeliverable(): 
    if checkLogin():
        return redirect("/logout")
    d=Deliverable()
    if 'itemID' in request.form:
        if len(request.form['itemID']) >0:
            d.retreive(int(request.form['itemID']))
    tasks=request.form.getlist('tasks[]')
    requirments=request.form.getlist('requirments[]')
    d["title"]=request.form['itemName']
    d["description"]=request.form['description']
    d["due_date"]=request.form['due_date']
    if 'itemID' in request.form:
        if len(request.form['itemID']) >0:
            unAssociateTasks(request.form['itemID'])
            unAssociateRequirments(request.form['itemID'])
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
    for requirment in requirments:
        r=Requirment()
        r.retreive(int(requirment))
        r['deliverable_id']=d['id']
        r.deleteRemote()
        r.create()
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
def unAssociateRequirments(deliverableID):
    t=Requirment()
    associatedRequirments=t.retreiveWithDeliverable(int(deliverableID))
    for requirmentid in associatedRequirments:
        requirment=Requirment()
        requirment.retreive(requirmentid['id'])
        requirment["deliverable_id"]=None
        requirment.deleteRemote()
        requirment.create()
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
    return  render_template('createTask.jinja', page='Tasks',task=None,issues=Issue().retreiveAll(),resources=Resource().retreiveAll(),tasks=Task().retreiveAll(),deliverables=Deliverable().retreiveAll())
@app.route('/TasksEdit',methods = ['GET'])
def editTask(): 
    if checkLogin():
        return redirect("/logout")
    id = request.args['id']
    t=Task()
    t.retreive(id)
    issuesAssignedObj=task_issue().retreiveWitTask(id)
    issuesAssigned=[]
    print(issuesAssignedObj)
    for issue in issuesAssignedObj:
        issuesAssigned.append(issue["issue_id"])
    issues=Issue().retreiveAll()
    resources=Resource().retreiveAll()
    resourcesAssignedObj=task_resource().retreiveWitTask(id)
    resourcesAssigned=[]
    print(resourcesAssignedObj)
    for resource in resourcesAssignedObj:
        resourcesAssigned.append(resource["resource_id"])
    predTasksObj=task_pred().retreiveWitTask(id)
    predTasks=[]
    print(predTasksObj)

    for task in predTasksObj:
        predTasks.append(task["predecessor_id"])
    succTasksObj=task_succ().retreiveWitTask(id)
    succTasks=[]
    print(succTasksObj)

    for task in succTasksObj:
        succTasks.append(task["successor_id"])
    return  render_template('createTask.jinja', page='Tasks',task=t,issuesAssigned=issuesAssigned,issues=issues,resourcesAssigned=resourcesAssigned,resources=resources,predTasks=predTasks,succTasks=succTasks,tasks=Task().retreiveAll(),deliverables=Deliverable().retreiveAll())
@app.route('/TasksDelete',methods = ['GET'])
def deleteTask(): 
    if checkLogin():
        return redirect("/logout")
    id = request.args['id']
    t=Task()
    t.retreive(id)
    t.delete()
    return tasks()
@app.route('/saveTask',methods = ['POST'])
def saveTask(): 
    if checkLogin():
        return redirect("/logout")
    print(request.form)

    t=Task()
    predTasksObj=task_pred()
    succTasksObj=task_succ()
    associatedIssuesObj=task_issue()
    associatedResourcesObj=task_resource()
    oldPredTasks=[]
    oldSuccTasks=[]
    if 'itemID' in request.form:
        if len(request.form['itemID']) >0:
            t.retreive(int(request.form['itemID']))
            predTasksObj.deleteRemote(t["id"])
            succTasksObj.deleteRemote(t["id"])
            oldPredTasks=task_pred().retreiveWitPredTask(int(request.form['itemID']))
            oldSuccTasks=task_succ().retreiveWitSuccTask(int(request.form['itemID']))
            task_pred().deleteRemotePredTask(int(request.form['itemID']))
            task_succ().deleteRemoteSuccTask(int(request.form['itemID']))
            associatedIssuesObj.deleteRemoteTask(t["id"])
            associatedResourcesObj.deleteRemoteTask(t["id"])
            t.deleteRemote()
    predTasks=request.form.getlist('predTasks[]')
    succTasks=request.form.getlist('succTasks[]')
    associatedIssues=request.form.getlist('issues[]')
    associatedResources=request.form.getlist('resources[]')
    t["title"]=request.form['itemName']
    t["description"]=request.form['description']
    t["type"]=request.form['type']
    t["expected_effort"]=request.form['expected_effort']
    t["actual_effort"]=request.form['actual_effort']
    t["expected_duration"]=request.form['expected_duration']
    t["actual_duration"]=request.form['actual_duration']
    t["effort_completed"]=request.form['effort_completed']
    t["percent_complete"]=request.form['percent_complete']
    if 'deliverable' in request.form:
        t["deliverable_id"]=request.form['deliverable']
    t.create()
    if 'itemID' in request.form:
        if len(request.form['itemID']) <= 0:
            t.retreiveMostRecent()
    for task in predTasks:
        predTasksObj["task_id"]=t["id"]
        predTasksObj["predecessor_id"]=task
        predTasksObj.create()
    for task in succTasksObj:
        succTasksObj["task_id"]=t["id"]
        succTasksObj["successor_id"]=task
        succTasksObj.create()
    for relation in oldSuccTasks:
        succTasksObj=task_succ()
        succTasksObj["task_id"]=relation["task_id"]
        succTasksObj["successor_id"]=relation["successor_id"]
        succTasksObj.create()
    for relation in oldPredTasks:
        predTasksObj=task_pred()
        predTasksObj["task_id"]=relation["task_id"]
        predTasksObj["predecessor_id"]=relation["predecessor_id"]
        predTasksObj.create()
    for issue in associatedIssues:
        associatedIssuesObj["task_id"]=t["id"]
        associatedIssuesObj["issue_id"]=issue
        associatedIssuesObj.create()
    for resource in associatedResources:
        associatedResourcesObj["task_id"]=t["id"]
        associatedResourcesObj["resource_id"]=resource
        associatedResourcesObj.create()
    return redirect("/tasks")
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
    return  render_template('dashboard.jinja', title='hello '+ session['username'], page='Requirments',items=Requirment().retreiveAll())

@app.route('/RequirmentsEdit',methods = ['GET'])
def editRequirment(): 
    if checkLogin():
        return redirect("/logout")
    print(request.args['id'])
    print("\n")
    r=Requirment()
    r.retreive(request.args['id'])
    print(r)
    return  render_template('createRequirment.jinja', page='Requirments',requirment=r,deliverables=Deliverable().retreiveAll())
@app.route('/createRequirment')
def createRequirment(): 
    if checkLogin():
        return redirect("/logout")
    return  render_template('createRequirment.jinja', page='Requirments',requirment=None,deliverables=Deliverable().retreiveAll())
@app.route('/RequirmentsDelete',methods = ['GET'])
def deleteRequirment(): 
    if checkLogin():
        return redirect("/logout")
    id = request.args['id']
    r=Requirment()
    r.retreive(id)
    r.delete()
    return requirments()
@app.route('/saveRequirment',methods = ['POST'])
def saveRequirment(): 
    if checkLogin():
        return redirect("/logout")
    r=Requirment()
    if 'itemID' in request.form:
        if len(request.form['itemID']) >0:
            r.retreive(int(request.form['itemID']))
            r.deleteRemote()
    r["title"]=request.form['itemName']
    if 'deliverable' in request.form:
        r["deliverable_id"]=request.form['deliverable']
    r.create()
    
    return redirect("/requirments")
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
