from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy

from config import db

# Models go here!
# server/models.py
from server.config import db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

# User Model: This stores the user info, such as username and password.
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    reviews = db.relationship('Review', backref='user', lazy=True)  # One-to-many relationship with Review

    def __repr__(self):
        return f"<User {self.username}>"

# Book Model: This stores the book details.
class Book(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String(100), nullable=True)
    reviews = db.relationship('Review', backref='book', lazy=True)  # One-to-many relationship with Review

    def __repr__(self):
        return f"<Book {self.title} by {self.author}>"

# Review Model: This stores the reviews for books, including ratings.
class Review(db.Model):
    __tablename__ = 'reviews'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(1000), nullable=False)
    rating = db.Column(db.Integer, nullable=False)  # Rating from 1-5
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return f"<Review for {self.book.title} by {self.user.username}>"

 # Method to hash the password before storing it
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    # Method to check the hashed password
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)