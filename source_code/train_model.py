import os
import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report
from preprocess import clean_text

def train():
    print("Loading dataset...")
    df = pd.read_csv('../dataset/sentiment_dataset.csv')
    print("Preprocessing text...")
    df['cleaned_text'] = df['text'].apply(clean_text)
    X_train, X_test, y_train, y_test = train_test_split(df['cleaned_text'], df['sentiment'], test_size=0.2, random_state=42)
    print("Vectorizing text using TF-IDF...")
    vectorizer = TfidfVectorizer(max_features=5000)
    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec = vectorizer.transform(X_test)
    print("Training Logistic Regression model...")
    model = LogisticRegression(random_state=42)
    model.fit(X_train_vec, y_train)
    print("Evaluating model...")
    y_pred = model.predict(X_test_vec)
    acc = accuracy_score(y_test, y_pred)
    prec = precision_score(y_test, y_pred, average='macro', zero_division=0)
    rec = recall_score(y_test, y_pred, average='macro', zero_division=0)
    f1 = f1_score(y_test, y_pred, average='macro', zero_division=0)
    cm = confusion_matrix(y_test, y_pred)
    report = classification_report(y_test, y_pred, zero_division=0)
    results = f"""Model Evaluation Results:
Accuracy:  {acc:.4f}
Precision: {prec:.4f}
Recall:    {rec:.4f}
F1-Score:  {f1:.4f}

Confusion Matrix:
{cm}

Classification Report:
{report}
"""
    print(results)
    with open('vectorizer.pkl', 'wb') as f:
        pickle.dump(vectorizer, f)
    with open('model.pkl', 'wb') as f:
        pickle.dump(model, f)
    print("Model and vectorizer saved successfully.")
    os.makedirs('../output', exist_ok=True)
    with open('../output/results.txt', 'w', encoding='utf-8') as f:
        f.write(results)

if __name__ == '__main__':
    train()
