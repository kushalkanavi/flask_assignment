from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

from models import db

from assignment.urls import assignment

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/flaskdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.app = app
db.init_app(app)

app.register_blueprint(assignment, url_prefix='/assignment')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
