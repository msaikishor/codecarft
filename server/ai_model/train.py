import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# Mock data
examples = [
    {"text": "Reverse a string in Python", "difficulty": "easy"},
    {"text": "Implement Dijkstra algorithm", "difficulty": "hard"},
    {"text": "Find median of sorted array", "difficulty": "medium"},
    {"text": "Merge k sorted lists", "difficulty": "hard"},
]

texts = [e['text'] for e in examples]
labels = [e['difficulty'] for e in examples]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)

model = MultinomialNB()
model.fit(X, labels)

with open('model.pkl', 'wb') as f:
    pickle.dump({'model': model, 'vectorizer': vectorizer}, f)

print("Model trained and saved as model.pkl")
