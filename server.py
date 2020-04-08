from flask import Flask
from flask import render_template
from flask import request
from flask import Flask, redirect, url_for, request

app = Flask(__name__)

@app.route("/")
def index():
    return  render_template('index.jinja', title='Welcome')
@app.route('/login',methods = ['POST'])
def login():
    user = request.form.get('username')
    password= request.form.get('pass')
    print(user)
    print(password)
    if user=="user" and password =="password":
        return render_template('login.jinja')
    return render_template('test.html')


if __name__ == "__main__":
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True,host= '0.0.0.0')
