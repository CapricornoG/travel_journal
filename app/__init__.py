import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate
from dotenv import load_dotenv

# Initialize extensions
db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
migrate = Migrate()

def create_app():
    """
    Factory function to create the Flask application and initialize extensions.
    This function loads environment variables, sets up Flask extensions, and
    registers blueprints.
    """
    # Load environment variables from a .env file
    load_dotenv()

    # Create Flask application
    app = Flask(__name__)

    # Configure Flask application
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

    # Handle different environments for DATABASE_URL
    if os.environ.get('DEVELOPMENT') == 'True':
        # For local development, use a local database URL
        app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URL')
    else:
        # For production on Heroku, use the DATABASE_URL from the environment
        uri = os.getenv('DATABASE_URL')  # Get the Heroku DATABASE_URL
        if uri and uri.startswith('postgres://'):
            uri = uri.replace('postgres://', 'postgresql://', 1)  # Adjust for SQLAlchemy
        app.config['SQLALCHEMY_DATABASE_URI'] = uri

    # Initialize Flask extensions
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)

    # Set up Flask-Login configuration
    login_manager.login_view = 'main.login'
    login_manager.login_message_category = 'info'

    # Register blueprints
    from app.routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
