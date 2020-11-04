from app import db
from datetime import datetime
# hashing
from werkzeug.security import generate_password_hash, check_password_hash
# Flask login
from flask_login import UserMixin
from app import login

# user loader function
@login.user_loader
def load_user(id):
    return User.query.get(int(id))


# Class to define the user table 
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    # function for setting the hashing 

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    # comparing the user password with the database stored hashed password
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


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