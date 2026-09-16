# Sentiment Analysis System

## Student Details

| Field         | Details                                             |
| ------------- | --------------------------------------------------- |
| Student Name  | Vansh Chunarkar                                     |
| Roll No./BTID | BT240016ET                                          |
| Branch        | ETC — Electronics and Telecommunication Engineering |
| Semester      | V Semester                                          |
| Course        | Natural Language Processing (ET5M004)               |
| Activity      | Creating GitHub Repositories                        |

## GitHub Repository

[https://github.com/vanshchunarkar-stack/SmartSentiment-Sentiment-Analysis-System](https://github.com/vanshchunarkar-stack/SmartSentiment-Sentiment-Analysis-System)

============================================================
## Project Overview

Natural Language Processing (NLP) enables computers to process and analyze human language. This project implements a **Sentiment Analysis System** that classifies input text into one of three categories: Positive, Negative, or Neutral. 

Sentiment analysis is highly useful in the real world for understanding user feedback, product reviews, and public opinions on social media. This project solves the problem of manually reading and interpreting large volumes of text by automating the classification process using classical machine learning and NLP techniques. 

The system implements a supervised learning approach for multi-class classification.

============================================================
## Problem Statement

Analyzing public sentiment from text data is crucial for understanding user feedback and opinions. Manual analysis of thousands of reviews or comments is slow, tedious, and unscalable. This project aims to automatically classify text sentiment using NLP techniques and classical machine learning, providing immediate feedback on whether a statement is positive, negative, or neutral.

============================================================
## Objectives

• Accept textual input from the user.
• Preprocess the text to remove noise (punctuation, capitalization).
• Tokenize the sentences into individual words.
• Remove unnecessary stop-words.
• Extract useful numerical features using TF-IDF vectorization (including unigrams and bigrams).
• Train a Logistic Regression model to classify sentiment.
• Provide an interactive web-based user interface for live text analysis.
• Display the predicted sentiment result to the user.

============================================================
## Introduction to NLP

Natural Language Processing (NLP) is a branch of Artificial Intelligence that allows computers to understand, interpret, and manipulate human language. It bridges the gap between human communication and computer understanding.

In this project, NLP is applied to transform unstructured human text (like reviews or comments) into structured numerical data. This structured data is then used to train a machine learning model capable of predicting the underlying emotional tone (sentiment) of new, unseen text.

============================================================
## Type of Classification

### Sentiment Classification

This project implements **Multi-class Sentiment Classification**. Instead of generating new text, the system categorizes the input text into one of three predefined classes:
- **Positive**: Text expressing a favorable or happy emotion.
- **Negative**: Text expressing an unfavorable or angry emotion.
- **Neutral**: Text expressing a factual or emotionless statement.

This is a discriminative task where the model learns the boundaries between these categories based on word frequencies.

============================================================
## NLP Techniques Used

| Technique             | Purpose                                      |
| --------------------- | -------------------------------------------- |
| Text Cleaning         | Removes unnecessary noise (punctuation, cases)|
| Word Tokenization     | Splits sentences into individual words       |
| Stop-word Removal     | Removes less informative words (e.g., 'the') |
| Feature Extraction    | Converts text into useful numerical features |
| Model Training        | Learns patterns from the numerical features  |
| Prediction            | Classifies the sentiment of new text         |

============================================================
## Methodology

The project follows a standard NLP classification workflow:

Input Text
↓
Text Preprocessing (Lowercasing, Punctuation Removal)
↓
Word Tokenization
↓
Stop-word Removal
↓
Feature Extraction (TF-IDF Vectorization)
↓
Model Prediction (Logistic Regression)
↓
Final Sentiment Result (Positive/Negative/Neutral)

============================================================
## Text Preprocessing

The preprocessing pipeline ensures that the machine learning model focuses on meaningful words rather than noise. The implemented steps are:
1. **Lowercasing**: All text is converted to lowercase to treat words like "Good" and "good" identically.
2. **Punctuation Removal**: Special characters and punctuation marks are stripped using regular expressions.
3. **Word Tokenization**: The text is split into a list of individual words using the NLTK `word_tokenize` function.
4. **Stop-word Removal**: Common but uninformative words (e.g., "is", "the", "and") are removed using the NLTK English stopwords corpus.

============================================================
## Feature Extraction

The project uses **TF-IDF (Term Frequency-Inverse Document Frequency)** to extract features. The model also extracts both unigrams (single words) and bigrams (two-word phrases) up to a maximum of 10,000 features.

- **TF (Term Frequency)**: Measures how frequently a word appears in a document.
- **IDF (Inverse Document Frequency)**: Measures how important a word is across the entire dataset. It penalizes very common words and rewards rare, distinctive words.
- **TF-IDF**: The product of TF and IDF. It assigns a high weight to words that are frequent in a specific text but rare overall, helping the model identify sentiment-defining words.

============================================================
## Model Training and Prediction

The system utilizes a **Logistic Regression** model for classification. 
During training, the model learns the weights associated with each TF-IDF feature for the three sentiment classes. When new text is inputted, the system processes the text, converts it to a TF-IDF vector, and passes it to the Logistic Regression model, which predicts the class with the highest probability.

============================================================
## User Interface

The project features a web-based user interface built with **Streamlit**.
- **Text Input Area**: A text box where users can type or paste sentences for analysis.
- **Generate Button**: An "Analyze Sentiment" button to trigger the NLP pipeline.
- **Result Display**: The interface outputs the predicted sentiment dynamically formatted with colors (Green for Positive, Red for Negative, Blue for Neutral).
- **Error Handling**: Displays a warning if the user clicks the button without entering any text.

============================================================
## Technologies and Libraries

| Technology   | Purpose                      |
| ------------ | ---------------------------- |
| Python       | Main programming language    |
| NLTK         | NLP preprocessing and tokenization |
| scikit-learn | Feature extraction and model training |
| Streamlit    | Web-based user interface     |
| NumPy        | Numerical processing         |
| pandas       | Dataset processing           |

============================================================
## Project Structure

```
SmartSentiment-Sentiment-Analysis-System/
│
├── README.md                  # Project documentation
├── requirements.txt           # Python dependencies
├── .gitignore                 # Ignored files for Git
├── dataset/                   # Folder containing the dataset
│   └── sentiment_dataset.csv  # The CSV dataset used for training
├── source_code/               # Main application code
│   ├── preprocess.py          # Functions for text cleaning
│   ├── train_model.py         # Script to train and save the model
│   ├── predict.py             # Script for CLI prediction testing
│   ├── app.py                 # Streamlit web application
│   ├── vectorizer.pkl         # Saved TF-IDF vectorizer
│   └── model.pkl              # Saved Logistic Regression model
├── notebooks/                 # Jupyter notebooks for experimentation
│   └── SmartSentiment_Analysis.ipynb
├── output/                    # Model evaluation outputs
│   └── results.txt            # Training evaluation metrics
└── screenshots/               # Directory for UI screenshots
```

============================================================
## Installation

To install and run the project locally, run the following commands:

```bash
git clone https://github.com/vanshchunarkar-stack/SmartSentiment-Sentiment-Analysis-System.git
cd SmartSentiment-Sentiment-Analysis-System
```

Create and activate a virtual environment:
```bash
python -m venv venv
# Windows:
.\venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
```

Install the required dependencies:
```bash
pip install -r requirements.txt
```

============================================================
## Execution

To start the Streamlit web application:

```bash
streamlit run source_code/app.py
```

To retrain the model on new data:
```bash
cd source_code
python train_model.py
```

============================================================
## How the System Works

1. User enters text into the Streamlit web interface.
2. The user clicks "Analyze Sentiment".
3. The system validates the input to ensure it is not empty.
4. The text is passed to the preprocessing pipeline (lowercased, punctuation removed).
5. The text is tokenized into words and stop-words are removed.
6. The cleaned text is transformed into a numerical vector using the saved TF-IDF vectorizer.
7. The Logistic Regression model predicts the sentiment class based on the vector.
8. The predicted sentiment (Positive, Negative, or Neutral) is displayed on the UI.

============================================================
## Results and Observations

The model was evaluated using standard classification metrics:
- **Accuracy**: Indicates the overall correctness of the model.
- **Precision**: Measures how many of the positively predicted instances were actually correct.
- **Recall**: Measures how many of the actual positive instances were successfully predicted.
- **F1-Score**: The harmonic mean of precision and recall.

Evaluation results (Accuracy, Precision, Recall, F1-Score, Confusion Matrix, and Classification Report) are generated and saved in `output/results.txt` upon running the training script. 

============================================================
## Edge Case Handling

The system handles several edge cases:
- **Empty Input**: The Streamlit interface detects empty input or spaces-only input and prompts the user with a warning: "Please enter some text to analyze."
- **Punctuation & Capitalization**: The preprocessing step normalizes capitalization and strips punctuation, ensuring "GREAT!" and "great" are treated identically.
- **Stop-words**: Sentences composed entirely of stop-words (e.g., "It is what it is") are heavily filtered; the model then defaults gracefully based on its learned intercept.

============================================================
## Advantages

- **Simple and efficient**: Uses a classical NLP pipeline (TF-IDF + Logistic Regression) which is fast to train and inference.
- **Lightweight**: Does not require heavy computation (GPUs) unlike deep learning models.
- **Interactive UI**: The Streamlit interface makes the model easily accessible to non-technical users.
- **Interpretable**: Unlike black-box neural networks, logistic regression weights can be inspected to see which words drive positive or negative sentiment.

============================================================
## Limitations

- **Context & Sarcasm**: The Bag-of-Words/TF-IDF approach ignores long-range word order and struggles to detect sarcasm or complex semantic context.
- **Dataset Size**: The current dataset is extremely small (41 lines). The model's accuracy is heavily bottlenecked by the lack of training data.
- **Out of Vocabulary Words**: Words that were not present in the training dataset will be ignored by the vectorizer during prediction.

============================================================
## Future Scope

- **Deep Learning Upgrade**: Implement Transformer-based models (like BERT) or LSTMs for better contextual understanding and higher accuracy.
- **Dataset Expansion**: Train the model on a massive real-world dataset (e.g., IMDb movie reviews, Twitter sentiment datasets).
- **Batch Processing**: Allow users to upload a CSV file in the Streamlit app to analyze the sentiment of hundreds of texts simultaneously.

============================================================
## Git and GitHub

### Git
Git is a distributed version control system used to track changes in the source code during project development. It ensures a complete history of all modifications.

### GitHub
GitHub is a cloud-based platform used to host Git repositories. It facilitates collaboration, code sharing, and academic portfolio building.

Multiple commits are used in this project to track the iterative development process, from initial setup to the integration of the Streamlit UI.

============================================================
## requirements.txt

The `requirements.txt` file specifies the exact Python packages required to run the project successfully, ensuring reproducibility across different environments. 

To install the packages:
```bash
pip install -r requirements.txt
```

============================================================
## .gitignore

The `.gitignore` file specifies intentionally untracked files that Git should ignore. 
In this project, it includes:
- `venv/` (Virtual environment files)
- `__pycache__/` (Compiled Python files)
This keeps the repository clean and prevents committing large, unnecessary environment files.

============================================================
## Academic Use

This project demonstrates the practical application of NLP concepts learned in the V Semester Natural Language Processing course. It showcases:
- NLP Text Preprocessing (Tokenization, Stop-word removal).
- Feature Extraction (TF-IDF vectorization).
- Machine Learning classification (Logistic Regression).
- Complete web-app deployment via Streamlit.
- Version control best practices using Git and GitHub.

============================================================
## Viva Preparation

1. **What is NLP?**
   Natural Language Processing is a field of AI that enables computers to understand, interpret, and process human language.
2. **What is Sentiment Analysis?**
   It is the computational task of categorizing text based on the emotional tone conveyed (e.g., positive, negative, neutral).
3. **What is Tokenization?**
   Tokenization is the process of splitting text into smaller units, such as words or sentences.
4. **What are Stop Words?**
   Common words (like 'is', 'the', 'and') that appear frequently but carry very little meaningful information for tasks like sentiment analysis.
5. **What is TF-IDF?**
   Term Frequency-Inverse Document Frequency is a statistical measure used to evaluate how important a word is to a document in a collection.
6. **Why was Logistic Regression selected?**
   It is a fast, interpretable, and effective baseline classification algorithm that works very well with sparse TF-IDF text features.
7. **Why was Streamlit used?**
   Streamlit allows rapid development of interactive web applications directly in Python without needing HTML/CSS/JS knowledge.
8. **What libraries were used?**
   NLTK for preprocessing, scikit-learn for modeling and feature extraction, pandas/numpy for data handling, and Streamlit for the UI.
9. **What are the limitations?**
   TF-IDF struggles with understanding word order, context, and sarcasm. The dataset size is also very limited.
10. **How can the project be improved?**
    By using a larger dataset and upgrading to deep learning architectures like BERT.
11. **How is GitHub used in this project?**
    To track code changes over time, backup the project, and showcase it for academic evaluation.

============================================================
## References

- Official Streamlit Documentation
- Official scikit-learn Documentation
- Official NLTK Documentation
