from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_swagger_ui import get_swaggerui_blueprint

from assignment.urls import assignment

from shared_models import db

app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/flaskdb'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
db.app = app
db.init_app(app)

### swagger specific ###
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Kaplan Flask Assignment"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
### end swagger specific ###

app.register_blueprint(assignment, url_prefix='/assignment')

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username

class Assignment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=False)
    type = db.Column(db.String(80), nullable=False)
    duration = db.Column(db.String(80), nullable=False)
    Assignment_Tag = db.relationship('Assignment_Tag_Map', backref='Assignment', lazy=True)

    def __init__(self, name, title, description, type, duration):
        self.name = name
        self.title = title
        self.description = description
        self.type = type
        self.duration = duration
        
    def __repr__(self):
        return '<Assignment %r>' % self.name

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    Assignment_Tag = db.relationship('Assignment_Tag_Map', backref='Tag', lazy=True)

    def __init__(self, name):
        self.name = name
        
    def __repr__(self):
        return '<Tag %r>' % self.name

class Assignment_Tag_Map(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    assignment_id = db.Column(db.Integer, db.ForeignKey('assignment.id'),nullable=False)
    tag_id = db.Column(db.Integer, db.ForeignKey('tag.id'),nullable=False)

    def __repr__(self):
        return '<Assignment_Tag_Map %r>' % self.id

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
