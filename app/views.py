from flask import render_template, request, redirect, make_response, flash
from app import app
from flask import g


app.secret_key = '*\x16\xb6\x1d\xa7\xe1\xde}\xaf\xa1\x8e>\xa5\x1c\x1a\x98\xabP;\x12\xd2\xa0\xaa\xa4'


# maybe login page should be different - but right now nothing to worry about
@app.route('/')
def landing():
    return render_template('index.html')
