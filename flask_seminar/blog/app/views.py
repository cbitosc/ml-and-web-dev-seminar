# views.py
from app import app, db
from flask import render_template, request
from . models import Post


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/add_post')
def add_post():
    return render_template('add_post.html')


@app.route('/added_post', methods=['POST'])
def added_post():
    author = request.form['Author']
    email = request.form['Email']
    post_added = Post(author=author, email=email)
    db.session.add(post_added)
    db.session.commit()

    return redirect(url_for('home', post_id=1))


# Display all your posts
@app.route('/post/<int:post_id>')
def post(post_id):
    post = Post.query.all()
    render_template('post.html', post=post)


# Write all your views here
