from flask import render_template, url_for, flash, redirect
from flaskblog import app
from flask_security import auth_required
#from flaskblog.forms import RegistrationForm, LoginForm
#from flaskblog.models import User, Post


@app.route("/")
#@app.route("/home")
@auth_required()
def home():
    return render_template('home.html')
