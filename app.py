from flask import Flask, request
from flask_restx import Api, Resource
from flask_cors import CORS
from models import db, Book
from schemas import ma, book_schema, books_schema
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

CORS(app)
db.init_app(app)
ma.init_app(app)

api = Api(app, doc='/swagger', title='Books API', description='CRUD API for books')

with app.app_context():
    db.create_all()

ns = api.namespace('books', description='Books CRUD')


@ns.route('/')
class BookList(Resource):
    def get(self):
        books = Book.query.all()
        return books_schema.dump(books), 200

    def post(self):
        new_book = book_schema.load(request.json)
        db.session.add(new_book)
        db.session.commit()
        return book_schema.dump(new_book), 201


@ns.route('/<string:id>')
class BookResource(Resource):
    def get(self, id):
        book = Book.query.get_or_404(id)
        return book_schema.dump(book), 200

    def put(self, id):
        book = Book.query.get_or_404(id)
        updated_book = book_schema.load(request.json, instance=book)
        db.session.commit()
        return book_schema.dump(updated_book), 200

    def delete(self, id):
        book = Book.query.get_or_404(id)
        db.session.delete(book)
        db.session.commit()
        return {'message': 'Deleted'}, 204


if __name__ == '__main__':
    app.run(debug=True, port=8000)