from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://lexwheels:cristian1122@lexwheels.mysql.pythonanywhere-services.com/db'

db = SQLAlchemy(app)

class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(30), unique=False, nullable=False)
    model = db.Column(db.String(30), unique=False, nullable=False)
    year = db.Column(db.Integer, unique=False, nullable=False)

    def __rep__(self):
        return f"Car('{self.id}', '{self.type}', '{self.model}')"

class Owner(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=False, nullable=False)

    def __rep__(self):
        return f"Owner('{self.id}', '{self.name}')"


@app.route('/')
def hello_world():
    return 'ok this app is working now'


@app.route('/details')
def details():
    return 'This website is about details'

@app.route('/car/<int:id>')
def car(id):
    return str(id)