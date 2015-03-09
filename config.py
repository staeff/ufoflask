import os
basedir = os.path.abspath(os.path.dirname(__file__))
DBUSER = os.environ.get("DBUSER", "")
PW = os.environ.get("PW", "")

# Path of the database file for Flask-SQLAlchemy
# SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
# DBUSER={user} PW={password} python routes.py
SQLALCHEMY_DATABASE_URI = 'mysql://{}:{}@localhost/ufosightings'.format(DBUSER,PW)
