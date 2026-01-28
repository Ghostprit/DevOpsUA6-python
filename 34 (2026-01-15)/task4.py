from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def displayPage():
    return render_template('task4templateOne.html')

@app.route('/image')
def displayImage():
    return render_template('task4templateTwo.html')