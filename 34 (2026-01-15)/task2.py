from flask import Flask
app = Flask(__name__)

@app.route('/')
def helloWorld():
    return 'Hello World!'

@app.route('/name/<name>')
def helloName(name):
    return 'Hello, %s!' % name