from app import app, db
from models import Hiragana, Katakana, Kanji
from flask import jsonify, render_template
from routes import *


# Route to get all Hiragana characters (API)
@app.route('/api/hiragana', methods=['GET'])
def get_hiragana():
    hiragana_list = Hiragana.query.all()
    return jsonify([
        {
            'id': h.id,
            'character': h.character,
            'romaji': h.romaji,
            'meaning': h.meaning,
            'pronunciation': h.pronunciation
        }
        for h in hiragana_list
    ])

# Route to get all Katakana characters (API)
@app.route('/api/katakana', methods=['GET'])
def get_katakana():
    katakana_list = Katakana.query.all()
    return jsonify([
        {
            'id': k.id,
            'character': k.character,
            'romaji': k.romaji,
            'meaning': k.meaning,
            'pronunciation': k.pronunciation
        }
        for k in katakana_list
    ])

# Route to get all Kanji characters (API)
@app.route('/api/kanji', methods=['GET'])
def get_kanji():
    kanji_list = Kanji.query.all()
    return jsonify([
        {
            'id': k.id,
            'character': k.character,
            'onyomi': k.onyomi,
            'kunyomi': k.kunyomi,
            'pronunciation': k.pronunciation
        }
        for k in kanji_list
    ])

# Route to render Hiragana page
@app.route('/hiragana', methods=['GET'])
def hiragana():
    return render_template('hiragana.html')

# Route to render Katakana page
@app.route('/katakana', methods=['GET'])
def katakana():
    return render_template('katakana.html')

# Route to render Kanji page
@app.route('/kanji', methods=['GET'])
def kanji():
    return render_template('kanji.html')
