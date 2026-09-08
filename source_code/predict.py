import pickle
import pandas as pd
from preprocess import clean_text

def load_model():
    with open('vectorizer.pkl', 'rb') as f:
        vectorizer = pickle.load(f)
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
    return vectorizer, model

def predict_sentiment(text, vectorizer, model):
    cleaned = clean_text(text)
    vec = vectorizer.transform([cleaned])
    prediction = model.predict(vec)[0]
    probabilities = model.predict_proba(vec)[0]
    classes = model.classes_
    confidence = max(probabilities)
    return prediction, confidence, dict(zip(classes, probabilities))

if __name__ == '__main__':
    vectorizer, model = load_model()
    test_cases = [
        "I absolutely love this product.",
        "This is the worst experience I have ever had.",
        "The product arrived yesterday."
    ]
    results = []
    for text in test_cases:
        sentiment, conf, probs = predict_sentiment(text, vectorizer, model)
        print(f"Text: '{text}'\nPredicted Sentiment: {sentiment.upper()}\nConfidence: {conf:.4f}\n")
        results.append({'text': text, 'predicted_sentiment': sentiment, 'confidence': conf})
    df = pd.DataFrame(results)
    df.to_csv('../output/sample_predictions.csv', index=False)
    print("Predictions saved to ../output/sample_predictions.csv")
