from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("hello.html")

import emoji

@app.route('/hello/')
def hello_world():
    return emoji.emojize('Hello me! :smiley:' , use_aliases=True)






