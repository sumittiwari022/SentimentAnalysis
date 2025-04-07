from flask import Flask, request, jsonify
import pickle
import re

app = Flask(__name__)

with open('/model/sentiment_model.pkl', 'rb') as f:
    model = pickle.load(f)
with open('/model/vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

def clean_text(text):
    return ' '.join(re.sub(r'[^a-zA-Z\s]', '', text.lower()).split())

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    text = data.get('text', '')
    cleaned_text = clean_text(text)
    vectorized_text = vectorizer.transform([cleaned_text])
    prediction = model.predict(vectorized_text)[0]
    sentiment = {0: 'Negative', 1: 'Neutral', 2: 'Positive'}[prediction]
    return jsonify({'sentiment': sentiment})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
