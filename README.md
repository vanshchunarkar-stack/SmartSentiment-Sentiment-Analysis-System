# SmartSentiment – Sentiment Analysis System Using NLP

**Student:** Vansh
**Roll No:** BT240016ET
**GitHub Username:** vanshchunarkar-stack
**Repository:** SmartSentiment-Sentiment-Analysis-System

## Project Overview
SmartSentiment is a complete college-level Natural Language Processing (NLP) application designed to classify text sentiment into Positive, Negative, or Neutral categories. This project demonstrates the full end-to-end NLP pipeline from data preprocessing to model training and interactive prediction.

## Problem Statement
Analyzing public sentiment from text data is crucial for understanding user feedback. Manual analysis is slow and unscalable. This project aims to automate sentiment classification using classical NLP techniques.

## Objectives
- Implement text cleaning and preprocessing (lowercasing, punctuation removal, stop-word removal, tokenization).
- Apply TF-IDF (Term Frequency-Inverse Document Frequency) feature extraction.
- Train a robust Logistic Regression classification model.
- Provide an interactive web UI using Streamlit for live text analysis.
- Evaluate the model using rigorous metrics (Accuracy, Precision, Recall, F1-Score).

## NLP Technique Used
- **Feature Extraction:** TF-IDF Vectorization
- **Algorithm:** Logistic Regression (Multi-class: One-vs-Rest)

## Dataset Information
A small, carefully labelled sample dataset sentiment_dataset.csv (20 samples) is included in the repository for testing and demonstration purposes. It contains text mapped to 'positive', 'negative', and 'neutral' labels.

## Technologies & Tools
- **Language:** Python 3
- **Libraries:** Scikit-learn, NLTK, Pandas, Numpy
- **UI Framework:** Streamlit
- **Environment:** Jupyter Notebook, Virtual Environment

## Methodology & Workflow
1. **Data Loading:** Read the dataset.
2. **Text Preprocessing:** Clean text, remove stopwords, and tokenize.
3. **Feature Extraction:** Convert text to numerical vectors using TfidfVectorizer.
4. **Model Training:** Train a LogisticRegression model on the vectors.
5. **Evaluation:** Calculate Accuracy, Precision, Recall, and F1-score on a test split.
6. **Prediction:** Accept new text, preprocess, vectorize, and predict sentiment via the Streamlit App.

## Project Structure
`
SmartSentiment-Sentiment-Analysis-System/
├── README.md
├── requirements.txt
├── .gitignore
├── dataset/
│   └── sentiment_dataset.csv
├── source_code/
│   ├── preprocess.py
│   ├── train_model.py
│   ├── predict.py
│   └── app.py
├── notebooks/
│   └── SmartSentiment_Analysis.ipynb
├── output/
│   ├── sample_predictions.csv
│   └── results.txt
├── screenshots/
│   └── README.md
└── docs/
    ├── project_methodology.md
    └── viva_questions.md
`

## Installation Requirements
`ash
# Create and activate a virtual environment
python -m venv venv
# Windows:
.\venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
`

## How to Run the Project

**1. Train the Model**
`ash
cd source_code
python train_model.py
`
*This will generate model.pkl and ectorizer.pkl.*

**2. Test the Model via CLI**
`ash
python predict.py
`

**3. Run the Streamlit Application**
`ash
streamlit run app.py
`

**4. Run the Jupyter Notebook**
`ash
cd ../notebooks
jupyter notebook SmartSentiment_Analysis.ipynb
`

## Results
- Evaluated on test split achieving high accuracy and robust F1-scores.
- Output metrics are saved in output/results.txt.
- Sample predictions are exported to output/sample_predictions.csv.

## Limitations
- The model relies on a classical Bag-of-Words approach (TF-IDF) which may not capture deep semantic context or sarcasm as effectively as deep learning models like BERT.
- The default dataset is a small sample for demonstration.

## Future Scope
- Integrate a larger, real-world dataset (e.g., IMDB or Twitter sentiment dataset).
- Upgrade to a deep learning model (LSTM or Transformer).
- Add functionality for file-upload based batch sentiment analysis in the UI.

## Conclusion
SmartSentiment successfully demonstrates the application of NLP for sentiment classification. It satisfies all college requirements for an end-to-end NLP project, featuring a clean architecture, rigorous evaluation, and an interactive user interface.
