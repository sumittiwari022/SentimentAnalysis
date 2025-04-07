import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle
import re

train_data = pd.read_csv('/model/train.csv', encoding='latin1')
test_data = pd.read_csv('/model/test.csv', encoding='latin1')
df = pd.concat([train_data, test_data]).dropna()

def clean_text(text):
    return ' '.join(re.sub(r'[^a-zA-Z\s]', '', str(text).lower()).split())

df['clean_text'] = df['text'].apply(clean_text)
vectorizer = TfidfVectorizer(max_features=5000)
X = vectorizer.fit_transform(df['clean_text'])
y = df['sentiment'].map({'negative': 0, 'neutral': 1, 'positive': 2})
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)
with open('/model/sentiment_model.pkl', 'wb') as f:
    pickle.dump(model, f)
with open('/model/vectorizer.pkl', 'wb') as f:
    pickle.dump(vectorizer, f)
print("Model training complete. Accuracy:", model.score(X_test, y_test))
