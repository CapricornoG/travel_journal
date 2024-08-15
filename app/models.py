from datetime import datetime
from app import db, login_manager
from flask_login import UserMixin
from werkzeug.utils import secure_filename
from flask import current_app
import os
import uuid

@login_manager.user_loader
def load_user(user_id):
    """Load user by ID."""
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    """Database model for a user."""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    journal_entries = db.relationship('JournalEntry', backref='author', lazy=True)

    def __repr__(self):
        """Representation of the User object."""
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class JournalEntry(db.Model):
    """Database model for a journal entry."""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    image_file = db.Column(db.String(255), nullable=True)  # Increased to 255 characters
    is_public = db.Column(db.Boolean, default=False, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        """Representation of the JournalEntry object."""
        return f"JournalEntry('{self.title}', '{self.date_posted}')"

    def save_image(self, image_file):
        """Saves the image to the filesystem and updates the image_file field."""
        if image_file:
            # Ensure the directory exists
            images_dir = os.path.join(current_app.root_path, 'static/images')
            if not os.path.exists(images_dir):
                os.makedirs(images_dir)

            # Create a unique filename using UUID to avoid conflicts
            ext = os.path.splitext(image_file.filename)[1]  # Get the file extension
            filename = secure_filename(f"{uuid.uuid4().hex}{ext}")
            file_path = os.path.join(images_dir, filename)

            # Save the image
            image_file.save(file_path)

            # Update the image_file field with the filename
            self.image_file = filename
