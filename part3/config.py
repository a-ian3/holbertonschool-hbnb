import os

class Config:
    SECRET_KEY = 'secret'  # à changer en production
    SQLALCHEMY_DATABASE_URI = 'sqlite:///hbnb.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = 'jwt-secret'  # à changer en prod

