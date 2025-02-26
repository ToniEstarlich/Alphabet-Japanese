from app import app, db
from models import Hiragana, Katakana,  Kanji
from flask import jsonify

# Route to get all Hirana characters
@app.route('/api/hiragana', methods=['GET'])
def get_hiragana():
    hiragana_list = Hiragana.query.all()
    return jsonify([{'character': h.character, 'romaji': h.romaji, 'meaning': h.meaning} for h in hiragana_list])

# Route to get all Katakana characters
@app.route('/api/katakana', methods=['GET'])
def get_katakana():
    katakana_list = Katakana.query.all()
    return jsonify([{'character': k.character, 'romaji': k.romaji, 'meaning': k.meaning} for k in katakana_list])

# Route to get all Kanji characters
@app.route('/api/kanji', methods=['GET'])
def get_kanji():
    kanji_list = Kanji.query.all()
    return jsonify([{'character': k.character, 'onyomi': k.onyomi, 'kunyomi': k.kunyomi, 'meaning': k.meaning} for k in kanji_list])
  
