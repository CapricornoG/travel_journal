import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'fallback_secret_key')  # Use the secret key from env or a fallback
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///local.db')  # Use the database URL from env or fallback to SQLite
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Avoids SQLAlchemy event system overhead
