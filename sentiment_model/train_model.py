import joblib
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
import pandas as pd

# Load data
url = "https://raw.githubusercontent.com/dD2405/Twitter_Sentiment_Analysis/master/train.csv"
data = pd.read_csv(url)
data = data[['label', 'tweet']].dropna()

# Train model
X = data['tweet']
y = data['label']
vectorizer = CountVectorizer()
X_vec = vectorizer.fit_transform(X)
model = LogisticRegression()
model.fit(X_vec, y)

# Save model and vectorizer
joblib.dump(model, 'sentiment_model/model.joblib')
joblib.dump(vectorizer, 'sentiment_model/vectorizer.joblib')
