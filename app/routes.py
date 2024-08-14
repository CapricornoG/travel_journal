from flask import Blueprint, render_template, redirect, url_for, flash, request
from app import db, bcrypt, login_manager
from app.models import User, JournalEntry
from app.forms import RegistrationForm, LoginForm, JournalEntryForm, DeleteForm
from flask_login import login_user, current_user, logout_user, login_required

# Define the blueprint
main = Blueprint('main', __name__)

@main.route('/')
def home():
    public_entries = JournalEntry.query.filter_by(is_public=True).all()
    login_form = LoginForm()
    register_form = RegistrationForm()
    return render_template('home.html', public_entries=public_entries, login_form=login_form, register_form=register_form)

@main.route('/about')
def about():
    login_form = LoginForm()
    register_form = RegistrationForm()
    return render_template('about.html', login_form=login_form, register_form=register_form)

@main.route('/register', methods=['POST'])
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
        return redirect(url_for('main.home'))
    flash('Registration unsuccessful. Please check your details and try again.', 'danger')
    return redirect(url_for('main.home'))

@main.route('/login', methods=['POST'])
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
        flash('Login unsuccessful. Please check email and password', 'danger')
    else:
        flash('Login unsuccessful. Please check your details and try again.', 'danger')
    return redirect(url_for('main.home'))

@main.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.home'))

@main.route('/account')
@login_required
def account():
    delete_form = DeleteForm()
    login_form = LoginForm()
    register_form = RegistrationForm()
    return render_template('account.html', form=delete_form, login_form=login_form, register_form=register_form)


@main.route('/account/delete', methods=['POST'])
@login_required
def delete_account():
    user = User.query.get_or_404(current_user.id)
    db.session.delete(user)
    db.session.commit()
    flash('Your account has been deleted!', 'success')
    return redirect(url_for('main.home'))

@main.route('/journal/entries')
@login_required
def journal_entries():
    entries = JournalEntry.query.filter_by(author=current_user).all()
    login_form = LoginForm()
    register_form = RegistrationForm()
    return render_template('journal_entries.html', journal_entries=entries, login_form=login_form, register_form=register_form)

@main.route('/journal/entry/<int:entry_id>')
@login_required
def journal_entry(entry_id):
    entry = JournalEntry.query.get_or_404(entry_id)
    login_form = LoginForm()
    register_form = RegistrationForm()
    return render_template('journal_entry.html', journal_entry=entry, login_form=login_form, register_form=register_form)

@main.route('/journal/entry/<int:entry_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_journal_entry(entry_id):
    entry = JournalEntry.query.get_or_404(entry_id)
    if entry.author != current_user:
        flash('You do not have permission to edit this entry.', 'danger')
        return redirect(url_for('main.journal_entries'))

    form = JournalEntryForm()
    if form.validate_on_submit():
        entry.title = form.title.data
        entry.content = form.content.data
        entry.is_public = form.is_public.data
        db.session.commit()
        flash('Your journal entry has been updated!', 'success')
        return redirect(url_for('main.journal_entries'))
    elif request.method == 'GET':
        form.title.data = entry.title
        form.content.data = entry.content
        form.is_public.data = entry.is_public

    return render_template('edit_journal_entry.html', title='Edit Journal Entry', form=form)

@main.route('/journal/entry/<int:entry_id>/delete', methods=['POST'])
@login_required
def delete_journal_entry(entry_id):
    entry = JournalEntry.query.get_or_404(entry_id)
    if entry.author != current_user:
        flash('You do not have permission to delete this entry.', 'danger')
        return redirect(url_for('main.journal_entries'))

    db.session.delete(entry)
    db.session.commit()
    flash('Your journal entry has been deleted!', 'success')
    return redirect(url_for('main.journal_entries'))

@main.route('/journal/new', methods=['GET', 'POST'])
@login_required
def new_journal_entry():
    form = JournalEntryForm()
    login_form = LoginForm()
    register_form = RegistrationForm()
    
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
    
    return render_template('create_journal_entry.html', title='New Journal Entry', form=form, login_form=login_form, register_form=register_form)


@main.route('/journal/public')
def public_journal_entries():
    entries = JournalEntry.query.filter_by(is_public=True).all()
    return render_template('journal_entries.html', journal_entries=entries)

@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for('main.home'))
