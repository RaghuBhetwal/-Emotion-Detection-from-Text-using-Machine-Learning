import streamlit as st
import joblib

# loading the model
model = joblib.load('emotion_model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

st.title("Emotion Classifier")

# input for user
user_input = st.text_area("Enter your text")

if st.button("Predict Emotion"):
    if user_input:
        input_vec = vectorizer.transform([user_input])

        prediction = model.predict(input_vec)

        st.success(f"Predicted Emotion: {prediction[0]}")
    else:
        st.error("Please enter some text.")