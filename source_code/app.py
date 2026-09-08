import streamlit as st
import pickle
from preprocess import clean_text

@st.cache_resource
def load_resources():
    with open('vectorizer.pkl', 'rb') as f:
        vectorizer = pickle.load(f)
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
    return vectorizer, model

st.title("SmartSentiment – Sentiment Analysis System Using NLP")
st.write("Analyze the sentiment of any text. The system classifies text as **Positive**, **Negative**, or **Neutral**.")

vectorizer, model = load_resources()

user_input = st.text_area("Enter text here:", height=150)

if st.button("Analyze Sentiment"):
    if user_input.strip():
        cleaned = clean_text(user_input)
        vec = vectorizer.transform([cleaned])
        prediction = model.predict(vec)[0]
        probabilities = model.predict_proba(vec)[0]
        confidence = max(probabilities)
        st.subheader("Results")
        if prediction == 'positive':
            st.success(f"**Predicted Sentiment:** {prediction.upper()}")
        elif prediction == 'negative':
            st.error(f"**Predicted Sentiment:** {prediction.upper()}")
        else:
            st.info(f"**Predicted Sentiment:** {prediction.upper()}")
        st.write(f"**Confidence:** {confidence:.2%}")
        st.write("### Detailed Probabilities")
        classes = model.classes_
        for cls, prob in zip(classes, probabilities):
            st.write(f"- {cls.capitalize()}: {prob:.2%}")
    else:
        st.warning("Please enter some text to analyze.")
