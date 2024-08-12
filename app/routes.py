from flask import Blueprint, render_template, redirect, url_for, flash
from app import db
from app.models import User
from app.forms import RegistrationForm, LoginForm

# Define the blueprint
main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('home.html')

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # Handle registration logic here
        flash('Your account has been created!', 'success')
        return redirect(url_for('main.home'))
    return render_template('register.html', title='Register', form=form)

@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Handle login logic here
        flash('You have been logged in!', 'success')
        return redirect(url_for('main.home'))
    return render_template('login.html', title='Login', form=form)