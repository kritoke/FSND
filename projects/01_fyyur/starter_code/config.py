import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # Enable debug mode.
    DEBUG = True

    # Connect to the database

    SQLALCHEMY_DATABASE_URI = 'postgres://kritoke@localhost:5432/fyyur'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
