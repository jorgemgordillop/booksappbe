
# 📚 Flask Backend (Books Management API)

This is a RESTful API built with Flask, SQLAlchemy, and Flask-RESTx, allowing the management of books including functionalities to list, add, update, and delete book records.

---

## 🚀 Environment Requirements

- Python 3.12 or higher
- pip (usually included with Python)
- Virtual environment (`venv`) (optional but recommended)

---

## ⚙️ Installing Dependencies

Create and activate a virtual environment (recommended):

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

Then, install the dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the API locally

Run the server with:

```bash
python app.py
```

The backend API will be available at:
```
http://localhost:8000
```

Swagger documentation is accessible at:
```
http://localhost:8000/swagger
```

---

## 🐳 Running with Docker (Production)

Build the Docker image:

```bash
docker build -t backend-api .
```

Run the Docker container:

```bash
docker run -d -p 8000:8000 backend-api
```

Access the API at:

```
http://localhost:8000
```

---

## 📂 Project Structure

```
backend/
├── app.py
├── config.py
├── models.py
├── schemas.py
├── requirements.txt
├── Dockerfile
└── .gitignore
```

---

## 🛠️ Database Configuration

The backend uses PostgreSQL by default, configured in `config.py`:

```python
# config.py
class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://user:password@localhost:5432/booksdb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
```

If you prefer SQLite for local development, change `config.py` as follows:

```python
# config.py (SQLite)
class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///books.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
```

---

## 📋 API Endpoints

| Method | Endpoint           | Description                  |
|--------|--------------------|------------------------------|
| GET    | `/books/`          | Retrieve all books           |
| POST   | `/books/`          | Add a new book               |
| GET    | `/books/<id>`      | Retrieve a book by ID        |
| PUT    | `/books/<id>`      | Update a book by ID          |
| DELETE | `/books/<id>`      | Delete a book by ID          |

---

## 🚨 Common Issues

### CORS Issues:
The Flask API includes Flask-CORS for handling cross-origin requests. Ensure it is properly configured to accept requests from your frontend.

---

## 🤝 Contributing

1. Fork this repository.
2. Create your branch (`git checkout -b feature/new-feature`).
3. Commit your changes clearly (`git commit -m 'Add new feature'`).
4. Push to your branch (`git push origin feature/new-feature`).
5. Create a Pull Request.

---

## 📝 License

This project is licensed under the MIT License. Check the [LICENSE](LICENSE) file for more details.

