from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = { 'nickname': 'Michael' }
    posts = [
        {
            'author': { 'nickname': 'Steve' },
            'body': 'Beautiful day in Boca!'
        },
        {
            'author': { 'nickname': 'Susan' },
            'body': 'This blog is so cool!'
        }
    ]
    return render_template("index.html",
        title = 'Home',
        user = user, 
        posts = posts)
