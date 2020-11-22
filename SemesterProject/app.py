from flask import Flask
from flask import render_template
import logging

logging.basicConfig(filename='app.log',level=logging.DEBUG)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("hello.html")


@app.route('/hello/')
def hello_world():
    logging.info('Welcome to page 2!')
    return ('Hello Me!')
    

@app.route('/hiya/')
def hiya_world():
    logging.info('Going to page 3!')
    return ('Hiya everyone!')







