from flask import Flask, render_template, jsonify
from db import db  # Import db from db.py
from models import Hiragana, Katakana, Kanji  # Import models.py
import os

app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'postgresql://postgres:Toni2207@localhost/alphabet_japanese')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy with the Flask app
db.init_app(app)

# Create tables if they don’t exist
with app.app_context():
    db.create_all()

# Test route to check database connection
@app.route('/test-db')
def test_db():
    try:
        # Query a sample table, e.g., Hiragana, to see if it's connected
        hiragana_sample = Hiragana.query.first()  # Get the first record
        if hiragana_sample:
            return jsonify({
                "character": hiragana_sample.character,
                "romaji": hiragana_sample.romaji,
                "meaning": hiragana_sample.meaning
            })
        else:
            return jsonify({"message": "No Hiragana characters found."})
    except Exception as e:
        return jsonify({"error": str(e)})

# Route for the main overview page
@app.route('/')
def abc():
    return render_template('abc.html')

# Route for Hiragana page
@app.route('/hiragana')
def hiragana():
    # Query all Hiragana characters from the database
    hiragana_characters = Hiragana.query.all()
    return render_template('hiragana.html', characters=hiragana_characters)

# Route for Katakana page
@app.route('/katakana')
def katakana():
    # Query all Katakana characters from the database
    katakana_characters = Katakana.query.all()
    return render_template('katakana.html', characters=katakana_characters)

# Route for Kanji page
@app.route('/kanji')
def kanji():
    # Query all Kanji characters from the database
    kanji_characters = Kanji.query.all()
    return render_template('kanji.html', characters=kanji_characters)

if __name__ == '__main__':
    app.run(debug=True)
