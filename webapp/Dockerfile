FROM python:3.9
WORKDIR /app
COPY . .
COPY ../sentiment_model/ ./sentiment_model
RUN pip install flask scikit-learn joblib pandas
CMD ["python", "app.py"]
