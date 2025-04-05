from flask import Flask, request, render_template
import joblib

app = Flask(__name__)
model = joblib.load("sentiment_model/model.joblib")
vectorizer = joblib.load("sentiment_model/vectorizer.joblib")

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    if request.method == "POST":
        text = request.form.get("text")
        vec = vectorizer.transform([text])
        pred = model.predict(vec)[0]
        prediction = "Positive" if pred == 1 else "Negative"
    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
