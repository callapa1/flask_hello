from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'ok this app is working now'


@app.route('/details')
def details():
    number = 8
    return 'This website is about details'

