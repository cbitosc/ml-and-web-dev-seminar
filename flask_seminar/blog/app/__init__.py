#__init__.py
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
#We instantiate all the objects here

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)


from app import models,views 


#We import models and views after the initialisation to avoid circular imports







	
