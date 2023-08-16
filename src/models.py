from flask_sqlalchemy import SQLAlchemy
from flask import Flask

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

class Followers(db.Model):
    __tablename__ = 'followers'
    user_from_id= db.Column(db.Integer, db.ForeignKey('User.id'))
    user_to_id= db.Column(db.Integer, db.ForeignKey('User.id'))
   
class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True)
    user_id= db.Column(db.Integer, db.ForeignKey('User.id'))

class Media(db.Model):
    __tablename__ = 'media'
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.Enum)
    url = db.Column(db.String(250))
    post_id= db.Column(db.Integer, db.ForeignKey('Post.id'))


class Comment(db.Model):
    __tablename__ = 'comment'
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(250), nullable=True)
    author_id= db.Column(db.Integer, db.ForeignKey('User.id'))
    post_id= db.Column(db.Integer, db.ForeignKey('Poat.id'))



class Favorite(db.Model):
    __tablename__ = 'favorite'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    planet_id = db.Column(db.Integer, db.ForeignKey('planet.id'))
    character_id = db.Column(db.Integer, db.ForeignKey('character.id'))

    user = db.relationship('User', back_populates='favorites')
    planet = db.relationship('Planet', back_populates='favorites')
    character = db.relationship('Character', back_populates='favorites')


User.favorites = db.relationship('Favorite', back_populates='user')
Planet.favorites = db.relationship('Favorite', back_populates='planet')
Character.favorites = db.relationship('Favorite', back_populates='character')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run()