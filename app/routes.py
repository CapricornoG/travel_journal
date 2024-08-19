from flask import Blueprint, render_template, redirect, url_for, flash, request
from app import db, bcrypt, login_manager
from app.models import User, JournalEntry
from app.forms import RegistrationForm, LoginForm, JournalEntryForm, DeleteForm
from flask_login import login_user, current_user, logout_user, login_required

# Define the blueprint
main = Blueprint('main', __name__)

# Context processor to inject forms globally
@main.app_context_processor
def inject_forms():
    return {
        'login_form': LoginForm(),
        'register_form': RegistrationForm()
    }

@main.route('/')
def home():
    """Render the home page with public journal entries."""
    public_entries = JournalEntry.query.filter_by(is_public=True).all()
    return render_template('home.html', public_entries=public_entries)


@main.route('/about')
def about():
    """Render the about page."""
    return render_template('about.html')


@main.route('/register', methods=['POST'])
def register():
    """Register a new user."""
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
    """Log in an existing user."""
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

    return redirect(url_for('main.home'))


@main.route('/logout')
def logout():
    """Log out the current user."""
    logout_user()
    return redirect(url_for('main.home'))


@main.route('/account')
@login_required
def account():
    """Display account details and provide option to delete the account."""
    delete_form = DeleteForm()
    return render_template('account.html', form=delete_form)


@main.route('/account/delete', methods=['POST'])
@login_required
def delete_account():
    """Delete the current user's account."""
    user = User.query.get_or_404(current_user.id)
    
    # Manually delete all associated journal entries
    JournalEntry.query.filter_by(author=user).delete()

    # Now delete the user
    db.session.delete(user)
    db.session.commit()

    flash('Your account has been deleted!', 'success')
    return redirect(url_for('main.home'))


@main.route('/journal/entries', methods=['GET', 'POST'])
@login_required
def journal_entries():
    """List and filter journal entries."""
    search_query = request.args.get('search', '')
    filter_option = request.args.get('filter', '')

    # Query based on search and filter
    query = JournalEntry.query.filter_by(author=current_user)

    if search_query:
        query = query.filter(
            (JournalEntry.title.ilike(f'%{search_query}%')) |
            (JournalEntry.content.ilike(f'%{search_query}%'))
        )

    if filter_option == 'public':
        query = query.filter_by(is_public=True)
    elif filter_option == 'private':
        query = query.filter_by(is_public=False)

    entries = query.all()
    delete_form = DeleteForm()

    return render_template('journal_entries.html', journal_entries=entries, delete_form=delete_form)


@main.route('/journal/entry/<int:entry_id>')
@login_required
def journal_entry(entry_id):
    """Display a specific journal entry."""
    entry = JournalEntry.query.get_or_404(entry_id)
    delete_form = DeleteForm()

    return render_template('journal_entry.html', journal_entry=entry, form=delete_form)


@main.route('/journal/entry/<int:entry_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_journal_entry(entry_id):
    """Edit a specific journal entry."""
    entry = JournalEntry.query.get_or_404(entry_id)

    if entry.author != current_user:
        flash('You do not have permission to edit this entry.', 'danger')
        return redirect(url_for('main.journal_entries'))

    form = JournalEntryForm()

    if form.validate_on_submit():
        entry.title = form.title.data
        entry.content = form.content.data
        entry.is_public = form.is_public.data
        if form.image.data:
            entry.save_image(form.image.data)
        db.session.commit()
        flash('Your journal entry has been updated!', 'success')
        return redirect(url_for('main.journal_entries'))
    elif request.method == 'GET':
        form.title.data = entry.title
        form.content.data = entry.content
        form.is_public.data = entry.is_public

    return render_template(
        'journal_entry_form.html',
        title='Edit Journal Entry',
        form=form,
        journal_entry=entry,
        form_action=url_for('main.edit_journal_entry', entry_id=entry.id),
        submit_button_text='Update Entry'
    )


@main.route('/journal/entry/<int:entry_id>/delete', methods=['POST'])
@login_required
def delete_journal_entry(entry_id):
    """Delete a specific journal entry."""
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
    """Create a new journal entry."""
    form = JournalEntryForm()

    if form.validate_on_submit():
        journal_entry = JournalEntry(
            title=form.title.data,
            content=form.content.data,
            is_public=form.is_public.data,
            author=current_user
        )
        if form.image.data:
            journal_entry.save_image(form.image.data)
        db.session.add(journal_entry)
        db.session.commit()
        flash('Your journal entry has been created!', 'success')
        return redirect(url_for('main.journal_entries'))

    return render_template(
        'journal_entry_form.html',
        title='New Journal Entry',
        form=form,
        form_action=url_for('main.new_journal_entry'),
        submit_button_text='Create Entry'
    )


@main.route('/journal/public')
def public_journal_entries():
    """Display all public journal entries."""
    entries = JournalEntry.query.filter_by(is_public=True).all()
    return render_template('journal_entries.html', journal_entries=entries)


@login_manager.unauthorized_handler
def unauthorized():
    """Redirect unauthorized users to the home page."""
    return redirect(url_for('main.home'))