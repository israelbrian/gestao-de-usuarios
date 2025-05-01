from flask import Blueprint, render_template

home_rout = Blueprint('home', __name__)

@home_rout.route('/')
def home():
    return render_template('index.html')