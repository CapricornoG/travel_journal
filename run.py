from app import create_app
from config import Config  # Import the Config class from config.py
import os

app = create_app()
app.config.from_object(Config)  # Set the app configuration from the Config class

if __name__ == '__main__':
    # Use the PORT environment variable provided by Heroku
    port = int(os.environ.get('PORT', 5000))
    # Set debug to True only if running locally (development mode)
    debug = os.environ.get('FLASK_ENV') == 'development'
    app.run(host='0.0.0.0', port=port, debug=debug)
