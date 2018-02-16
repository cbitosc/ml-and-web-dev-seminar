#views.py
from app import app

@app.route('/')
def home():
	return '<H1> Your first MVC project</H1>'



#Write all your views here