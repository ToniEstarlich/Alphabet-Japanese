# Japanese Alphabet Web App
![Manga Gallery](static/images/kanji-screenshot.png)
## 📌 Project Overview
This is a web application designed to display **Hiragana, Katakana, and Kanji** characters along with their meanings and pronunciations. The application follows a **Flask (Python) back-end**, a **PostgreSQL database**, and an **HTML/CSS front-end**.

# Index:
# ⚙️ [back-end](#backend-flask--sqlalchemy)
# 🛢️  [Database](#database-postgresql--sqlalchemy)
# 🎨 [Front-end](#frontend-html-css-jinja2)

##  Project Structure
# 📂
```
Japanese-Alphabet/
│── static/         # CSS, images, and static files
│── templates/      # HTML templates
│── models.py       # Database models
│── db.py           # Database setup
│── app.py          # Main Flask application
│── models.py       # models setup
│── routes.py       # routes application
│── README.md       # Project documentation
```

---

## Backend (Flask & SQLAlchemy)
#  ⚙️
The **Flask framework** handles routes and communicates with the **PostgreSQL database** through **SQLAlchemy ORM**.

### 🔧 Setup Flask & Dependencies
1. Install dependencies:
   ```bash
   pip install flask flask-sqlalchemy psycopg2
   ```
2. Set up `app.py`:
   ```python
   from flask import Flask, render_template, jsonify
   from db import db  # Import database
   from models import Hiragana, Katakana, Kanji  # Import models
   import os

   app = Flask(__name__)
   app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'postgresql://postgres:Toni2207@localhost/alphabet_japanese')
   app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

   db.init_app(app)
   
   with app.app_context():
       db.create_all()
   ```
3. Run the app:
   ```bash
   python app.py
   ```

---

##  Database (PostgreSQL & SQLAlchemy)
#   🛢️
The application uses **PostgreSQL** with his **pgAdmin4** as the database, and **SQLAlchemy** as the ORM.

### 📌 Table Structure
Defined in `models.py`:
```python
from db import db

class Hiragana(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    character = db.Column(db.String(5), nullable=False)
    romaji = db.Column(db.String(20), nullable=False)
    meaning = db.Column(db.String(100))
```
(Similar models exist for **Katakana** and **Kanji**)

### 📥 Sample Data Insertion
After setting up the database, add records manually or through a script:
```python
hiragana_sample = Hiragana(character='あ', romaji='a', meaning='First character')
db.session.add(hiragana_sample)
db.session.commit()
```

---

##  FrontEnd (HTML, CSS, Jinja2)
#   🎨
The front-end is built using **HTML templates** with **Jinja2** to dynamically render database data.

### 📌 Example `hiragana.html`
```html
<!DOCTYPE html>
<html>
<head>
    <title>Hiragana</title>
    <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <h1>Hiragana Characters</h1>
    <ul>
        {% for char in characters %}
            <li>{{ char.character }} - {{ char.romaji }} - {{ char.meaning }}</li>
        {% endfor %}
    </ul>
</body>
</html>
```

---

## 🚀 Running the Project
1. Start PostgreSQL and ensure the database `alphabet_japanese` exists.
2. Run the Flask app:
   ```bash
   python app.py
   ```
3. Open in browser:
   ```
   http://127.0.0.1:5000/
   ```

---

## 🛠️ Debugging & Common Errors
- **`RuntimeError: The current Flask app is not registered with this SQLAlchemy instance`**
  - Ensure `db.init_app(app)` is correctly set.
  - Use `with app.app_context(): db.create_all()` to initialize tables.
- **`500 Internal Server Error`**
  - Check database connection and sample data.

---

## 📝 Conclusion
This project demonstrates how to integrate **Flask, SQLAlchemy, and PostgreSQL** to create a web app that displays **Japanese alphabet characters** dynamically. 🚀

