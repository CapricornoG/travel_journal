from flask import Blueprint, render_template, redirect, url_for, flash, request
from app import db, bcrypt, login_manager
from app.models import User, JournalEntry
from app.forms import RegistrationForm, LoginForm, JournalEntryForm
from flask_login import login_user, current_user, logout_user, login_required

# Define the blueprint
main = Blueprint('main', __name__)

@main.route('/')
def home():
    public_entries = JournalEntry.query.filter_by(is_public=True).all()
    return render_template('home.html', public_entries=public_entries)

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You can now log in', 'success')
        return redirect(url_for('main.login'))
    return render_template('register.html', title='Register', form=form)

@main.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.home'))
        else:
            flash('Login unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@main.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.home'))

@main.route('/account')
@login_required
def account():
    return render_template('account.html', title='Account')

@main.route('/journal/new', methods=['GET', 'POST'])
@login_required
def new_journal_entry():
    form = JournalEntryForm()
    if form.validate_on_submit():
        journal_entry = JournalEntry(
            title=form.title.data,
            content=form.content.data,
            is_public=form.is_public.data,
            author=current_user
        )
        db.session.add(journal_entry)
        db.session.commit()
        flash('Your journal entry has been created!', 'success')
        return redirect(url_for('main.journal_entries'))
    return render_template('create_journal_entry.html', title='New Journal Entry', form=form)

@main.route('/journal/entries')
@login_required
def journal_entries():
    entries = JournalEntry.query.filter_by(author=current_user).all()
    return render_template('journal_entries.html', journal_entries=entries)

@main.route('/journal/entry/<int:entry_id>')
@login_required
def journal_entry(entry_id):
    entry = JournalEntry.query.get_or_404(entry_id)
    return render_template('journal_entry.html', journal_entry=entry)

@main.route('/journal/public')
def public_journal_entries():
    entries = JournalEntry.query.filter_by(is_public=True).all()
    return render_template('journal_entries.html', journal_entries=entries)

@login_manager.unauthorized_handler
def unauthorized():
    return render_template('unauthorized.html'), 403
