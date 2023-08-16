from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from typing import List
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250), unique=True, nullable=False)
    email = db.Column(db.String(250), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)
    firstName = db.Column(db.String(250))
    lastName = db.Column(db.String(250))
    folowers_column: Mapped[List["Followers"]] = relationship()

class Followers(db.Model):
    __tablename__ = 'followers'
    id = db.Column(db.Integer, primary_key=True)
    User_id: Mapped[int] = mapped_column(ForeignKey("user.id"))

   
class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True)
    user_id= db.Column(db.Integer, db.ForeignKey('user.id'))

class Media(db.Model):
    __tablename__ = 'media'
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(250))
    url = db.Column(db.String(250))
    post_id= db.Column(db.Integer, db.ForeignKey('post.id'))


class Comment(db.Model):
    __tablename__ = 'comment'
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(250), nullable=True)
    author_id= db.Column(db.Integer, db.ForeignKey('user.id'))
    post_id= db.Column(db.Integer, db.ForeignKey('post.id'))





if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run()