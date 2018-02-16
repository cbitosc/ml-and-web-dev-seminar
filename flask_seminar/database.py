# database.py
import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
app = Flask(__name__)

# BASE_DIR = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(BASE_DIR, 'database.sqlite')

db = SQLAlchemy(app)


class SimpleDatabase(db.Model):
    name = db.Column(db.String(128), primary_key=True)
    email = db.Column(db.String(128), unique=True)

    def __repr__(self):
        return '<Name {}>,Email {}'.format(self.name, self.email)
