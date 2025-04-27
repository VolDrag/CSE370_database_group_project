from flask import Flask
from flask_login import LoginManager
from mysql.connector import connect, Error

# Initialize Flask-Login for user sessions
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)  # Correct initialization for the Flask app

    # Configuration
    app.config['SECRET_KEY'] = 'keyx'  # Change this to something secret!
    app.config['MYSQL_HOST'] = 'localhost'  # XAMPP typically uses localhost
    app.config['MYSQL_USER'] = 'root'  # MySQL default user for XAMPP
    app.config['MYSQL_PASSWORD'] = ''  # Default password for XAMPP MySQL is empty
    app.config['MYSQL_DB'] = 'stuarts_comic_shop'  # The name of your MySQL database

    # Initialize Flask-Login
    login_manager.init_app(app)  # Initialize Flask-Login for user session management

    # Import and register blueprints (routes)
    from app.routes.main_routes import main  # Import routes from main_routes.py
    app.register_blueprint(main)  # Register the blueprint with the app

    return app

# For Database Connection (using mysql-connector)
def get_db_connection():
    try:
        connection = connect(
            host='localhost',  # XAMPP MySQL host
            user='root',  # MySQL user for XAMPP
            password='',  # Password for XAMPP MySQL (empty by default)
            database='stuarts_comic_shop'  # Your database name
        )
        return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

connection = get_db_connection()
if connection:
    print("Connected to the database successfully!")
else:
    print("Failed to connect to the database.")