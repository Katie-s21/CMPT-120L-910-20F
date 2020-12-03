from flask import Flask
from flask import render_template
import logging

logging.basicConfig(filename='app.log',level=logging.DEBUG)

app = Flask(__name__)


@app.route('/')
def home():
    logging.info('Welcome to the Home Page!')
    return render_template('home.html')

@app.route('/personality')
def personality():
    app.logger.info("Switching to the Personality Page")
    return render_template("personality.html")
    
@app.route('/about/')
def about():
    logging.info('Going to the About Page!')
    return render_template('about.html')

@app.route('/contact/')
def contact():
    logging.info('Going to the Contact Page!')
    return render_template('contact.html')

@app.route('/404/')
def four_oh_four():
    app.logger.info("Switching to the 404 Page, This is a test page so we don't need to error here.")
    return render_template('four_oh_four.html')




