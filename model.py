# model.py
import re
import pickle

# Load model and vectorizer
with open("trained_model.sav", "rb") as f:
    model = pickle.load(f)

with open("tfidf_vectorizer.sav", "rb") as f:
    vectorizer = pickle.load(f)

def clean_text(text):
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    return text.lower()

def predict_sentiment(text):
    cleaned = clean_text(text)
    vector = vectorizer.transform([cleaned])
    prediction = model.predict(vector)[0]

    label_map = {
        0: "Negative",
        1: "Neutral",
        2: "Positive"
    }

    return label_map.get(prediction, "Unknown")

