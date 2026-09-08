# Project Methodology

This document explains the step-by-step methodology behind SmartSentiment.

## 1. Input Text
The system accepts raw string input from either a dataset (during training) or user input (during inference/app usage).

## 2. Text Preprocessing
Raw text contains noise. We clean it:
- **Lowercasing:** Converts all text to lowercase to ensure uniformity (e.g., "Good" and "good" are treated equally).
- **Punctuation Removal:** Strips out commas, periods, exclamation marks, etc. using Regular Expressions.

## 3. Tokenization & Cleaning
- **Tokenization:** Splits the sentence into individual words (tokens) using NLTK's word_tokenize.
- **Stop-word Removal:** Removes common English words (like "the", "is", "in") that do not carry significant sentiment meaning, reducing noise.

## 4. Feature Extraction (Vectorization)
Machine learning models cannot read text. We use **TF-IDF (Term Frequency-Inverse Document Frequency)** to convert text into numerical vectors.
- **TF:** How frequently a word appears in a document.
- **IDF:** How rare and informative the word is across all documents.
- The vectorizer assigns a numerical weight to each word, representing its importance.

## 5. Sentiment Classification
- We use **Logistic Regression**, a powerful baseline model for text classification.
- It calculates the probability of the input vector belonging to one of the three classes: Positive, Negative, or Neutral.

## 6. Prediction
For a new input, the model outputs the class with the highest probability.

## 7. Result
The final predicted sentiment and its confidence score are displayed to the user via the Streamlit interface or command line.
