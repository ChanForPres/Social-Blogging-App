# describe sqlite data models
from datetime import datetime
from app import db

'''
Models define inital DB structure for app

Migrations - Updating current DB w/o need to create from scratch
'''

class User(db.Model):
    # Assign ID as primary key - identifies other DB records
    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(64), index = True, unique = True)
    email = db.Column(db.String(120),index=True,unique=True)
    password_hash = db.Column(db.String(128))

    # Posts is not a User field,
    # defines relationship btwn User/Post
    # 1-> MANY
    # args: MANY object, backref= MANY object field pointing to User
    posts = db.relationship('Post',backref = 'author',lazy='dynamic')

    # print out object data
    def __repr__(self):
        return '<User {}>'.format(self.username)

class Post(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index = True, default = datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)

class Age(db.Model):
    value = db.Column(db.Integer,primary_key=True)

    def __repr__(self):
        return '<Age {}>'.format(self.value)
