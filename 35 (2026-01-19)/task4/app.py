from flask import Flask, render_template
from flask_caching import Cache

app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE': 'simple'})

@app.route('/')
@cache.cached(timeout=50)
def displayPage():
    return render_template('templateOne.html')

@app.route('/image')
@cache.cached(timeout=50)
def displayImage():
    return render_template('templateTwo.html')