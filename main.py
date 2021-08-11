from flask import Flask
from flask_mysqldb import MySQL
app = Flask(__name__)

app.config['MYSQL_HOST'] = 'lexwheels.mysql.pythonanywhere-services.com'
app.config['MYSQL_USER'] = 'lexwheels'
app.config['MYSQL_PASSWORD'] = 'cristian1122-'
app.config['MYSQL_DB'] = 'db'


@app.route('/')
def hello_world():
    return 'ok this app is working now'


@app.route('/details')
def details():
    number = 8
    return 'This website is about details'