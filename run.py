from app import create_app
from config import Config  # Import the Config class from config.py

app = create_app()
app.config.from_object(Config)  # Set the app configuration from the Config class

if __name__ == '__main__':
    app.run(debug=True)
