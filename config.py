import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'fallback_secret_key'  # Replace 'fallback_secret_key' with a backup key if needed
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///local.db'  # Default to a local SQLite database
    SQLALCHEMY_TRACK_MODIFICATIONS = False
