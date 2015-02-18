import os
basedir = os.path.abspath(os.path.dirname(__file__))

# Path of the database file for Flask-SQLAlchemy
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
