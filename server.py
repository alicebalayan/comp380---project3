from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return  render_template('index.jinja', title='Welcome')
@app.route("/test")
def test():
    return "Hello test!"


if __name__ == "__main__":
    app.run(host= '0.0.0.0')
