from flask import request, render_template, Response
from . import app

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api')
def api():
    return "asdf"
