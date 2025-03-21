from flask_sqlalchemy import SQLAlchemy
import uuid

db = SQLAlchemy()


class Book(db.Model):
    id = db.Column(db.String, primary_key=True, default=lambda: uuid.uuid4().hex)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    read = db.Column(db.Boolean, default=False)
