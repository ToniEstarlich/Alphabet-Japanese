# Step 5: Create API Routes to Serve Data

Next, in your `routes.py`, you can create endpoints to serve this data as JSON. Here's an example of how set up a simple API: 
```python
         from app import app, db
from models import Hiragana, Katakana, Kanji
from flask import jsonify

# Route to get all Hiragana characters
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

```
# Step 6: Run the Flask App

Now, run your Flask app:

```bash
  python app.py
```
The app shoud how we runing locally at `http://127.0.0.1:5000/` we can visit following end points: 

- `http://127.0.0.1:5000/api/hiragana`
- `http://127.0.0.1:5000/api/katakana`
- `http://127.0.0.1:5000/api/kanji`

these will return the **Hiragana**, **Katakana**, and **Kanji** characters in **JSON** format.