# Viva Questions & Answers

**1. What is NLP?**
Natural Language Processing (NLP) is a branch of artificial intelligence that focuses on enabling computers to understand, interpret, and generate human language.

**2. What is sentiment analysis?**
Sentiment analysis is the process of determining the emotional tone behind a series of words, used to gain an understanding of the attitudes, opinions, and emotions expressed.

**3. Why is sentiment analysis useful?**
It helps businesses understand customer feedback, monitor brand reputation, and automatically categorize reviews or social media posts as positive, negative, or neutral.

**4. What preprocessing is used in this project?**
Lowercasing, punctuation removal, tokenization, and stop-word removal.

**5. Why is text preprocessing necessary?**
Raw text is messy and contains noise (punctuation, irrelevant words). Preprocessing cleans the text, making it easier for the model to find meaningful patterns and reducing the dimensionality of the data.

**6. What is TF-IDF?**
TF-IDF stands for Term Frequency-Inverse Document Frequency. It's a numerical statistic that reflects how important a word is to a document in a collection or corpus.

**7. Why was Logistic Regression used?**
Logistic Regression is a robust, interpretable, and computationally efficient baseline algorithm that performs very well on high-dimensional sparse data like TF-IDF vectors.

**8. What is training data?**
The subset of data used to train the machine learning model, allowing it to learn the relationship between the text features and the sentiment labels.

**9. What is testing data?**
A separate subset of data not seen by the model during training. It is used to evaluate the model's performance on unseen data.

**10. What is accuracy?**
The ratio of correctly predicted observations to the total observations. 

**11. What are precision, recall, and F1-score?**
- **Precision:** Out of all positive predictions, how many were actually positive.
- **Recall:** Out of all actual positives, how many were correctly predicted.
- **F1-score:** The harmonic mean of Precision and Recall, providing a balance between them.

**12. What are the limitations of this system?**
It relies on a classical TF-IDF approach which ignores word order and deep context. Therefore, it might struggle with sarcasm or complex sentences compared to modern deep learning models.

**13. What happens when new text is entered in the app?**
The text is passed through the same preprocessing pipeline, vectorized using the saved TF-IDF vectorizer, and then the Logistic Regression model predicts the sentiment and confidence score.

**14. What are possible future improvements?**
Using a larger dataset, applying word embeddings (Word2Vec/GloVe), or using deep learning models like LSTMs or Transformers (BERT) for better contextual understanding.

**15. Explain the complete project workflow.**
Data Loading -> Preprocessing (cleaning/tokenizing) -> Feature Extraction (TF-IDF) -> Train-Test Split -> Model Training (Logistic Regression) -> Evaluation (Metrics/Confusion Matrix) -> Deployment (Streamlit App).
