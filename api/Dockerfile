FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app.py .
COPY model/sentiment_model.pkl model/vectorizer.pkl /model/
EXPOSE 5000
CMD ["python", "app.py"]