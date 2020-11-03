from app import db
from datetime import datetime

# Class to define the user table 
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(128))

# The method to print objects of this class 
# mainly for debbugging purposes 
    def __repr__(self):
        return '<User {}>'.format(self.username)

# class to define Post table
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

# The method to print objects of this class 
# mainly for debbugging purposes 
    def __repr__(self):
        return '<Post {}>'.format(self.body)  