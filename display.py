import streamlit as st
import requests

def predict_word(text):
    respond = requests.post("http://127.0.0.1:8000/predict_sentiment", json={"text": text})

    result_NB = respond.json()["predicted_sentiment_nb"]
    result_SVM = respond.json()["predicted_sentiment_svm"]
    accuracy_NB = respond.json()["accuracy_nb"]
    accuracy_SVM = respond.json()["accuracy_svm"]

    return result_NB, result_SVM, accuracy_NB, accuracy_SVM

st.title("Test API NLP")
text_to_predict = st.text_area("Input Text","isi dengan kalimat bahasa inggris")

# Button to predict sentiment
if st.button("Predict Sentiment"):
    result_nb, result_svm, acuracy_nb, acuracy_svm = predict_word(text_to_predict)
        # Display the predictions
    st.write(f"Predicted Sentiment (Naive Bayes) - {acuracy_nb} : {result_nb}")
    st.write(f"Predicted Sentiment (Linear SVM) - {acuracy_svm} : {result_svm}")