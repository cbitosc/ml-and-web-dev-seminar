#models.py
from app import db

# Here place all your ORM definitations and mapping tools


class Post(db.Model):
	author = db.Column(db.String(50))
	post = db.Column(db.Text)
	post_id = db.Column(db.Integer,primary_key=True)





