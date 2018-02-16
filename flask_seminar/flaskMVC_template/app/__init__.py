#__init__.py
from flask import Flask
#We instantiate all the objects here

app = Flask(__name__)
app.config.from_object('config')



from app import models,views 


#We import models and views after the initialisation to avoid circular imports







	
