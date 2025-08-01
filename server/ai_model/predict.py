import os
import pickle

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, 'model.pkl')

with open(MODEL_PATH, 'rb') as f:
    data = pickle.load(f)

model = data['model']
vectorizer = data['vectorizer']

def predict_difficulty(text):
    X = vectorizer.transform([text])
    return model.predict(X)[0]
