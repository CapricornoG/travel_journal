from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate  
from dotenv import load_dotenv
import os

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
migrate = Migrate() 

def create_app():
    load_dotenv()  
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)  

    from app.routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
