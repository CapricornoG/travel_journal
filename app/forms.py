from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.models import User
from flask_wtf.file import FileField, FileAllowed

class RegistrationForm(FlaskForm):
    """Form for users to create a new account."""
    username = StringField(
        'Username', 
        validators=[DataRequired(), Length(min=2, max=20)]
    )
    email = StringField(
        'Email', 
        validators=[DataRequired(), Email()]
    )
    password = PasswordField(
        'Password', 
        validators=[DataRequired()]
    )
    confirm_password = PasswordField(
        'Confirm Password', 
        validators=[DataRequired(), EqualTo('password')]
    )
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        """Validate if the username already exists."""
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        """Validate if the email already exists."""
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')

class LoginForm(FlaskForm):
    """Form for users to log in."""
    email = StringField(
        'Email', 
        validators=[DataRequired(), Email()]
    )
    password = PasswordField(
        'Password', 
        validators=[DataRequired()]
    )
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class JournalEntryForm(FlaskForm):
    """Form for creating or editing a journal entry with an optional image."""
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    image = FileField('Upload Image', validators=[FileAllowed(['jpg', 'png'])])
    is_public = BooleanField('Make Public')
    submit = SubmitField('Post')

class DeleteForm(FlaskForm):
    """Form for deleting a user account."""
    submit = SubmitField('Delete Account')