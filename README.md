#  Emotion Detection from Text using Machine Learning

This project is a text classification application that uses **Logistic Regression** to detect emotions such as **joy**, **anger**, **sadness**, **fear**, **love**, and **surprise** from a given sentence. It uses **TF-IDF Vectorization** and **NLTK** for text preprocessing, and includes a **Streamlit web interface** for real-time predictions.

---

##  Project Highlights

- 🔹 **Dataset:** Emotion Dataset (train/test split)
- 🔹 **Preprocessing:** Tokenization, Stopword Removal, and Stemming using NLTK
- 🔹 **Vectorization:** TF-IDF (Term Frequency-Inverse Document Frequency)
- 🔹 **Model:** Logistic Regression from Scikit-learn
- 🔹 **Evaluation Metrics:** Accuracy, Precision, Recall, F1-Score, Confusion Matrix
- 🔹 **Interface:** emotion prediction with Streamlit
- 🔹 **Persistence:** Model and Vectorizer saved using Joblib

---

## 🗂️ Project Structure
```
├── app.py                  # Streamlit application

data/
   ├── train.txt               # Training data
   ├── test.txt                # Testing data
   
├── emotion_model.pkl       # Trained Logistic Regression model

├── vectorizer.pkl          # TF-IDF Vectorizer

└── README.md               # Project overview
```

## Streamlite UI /Prediction

<p align="center"> <img src="https://github.com/user-attachments/assets/214383ce-c1b3-4817-abac-5ad2911e3ec3" alt="Streamlit Input Interface" width="600"/> </p>
-----------------------------------------------------------------------------------------------------------------------------------------------------------
<p align="center"> <img src="https://github.com/user-attachments/assets/86c54e01-4e4c-4227-8311-b80a8666f18f" alt="Streamlit Prediction Output" width="600"/> </p>


# Future Work

🔹 Expand Emotion Categories: Adding more emotional categories for better coverage

🔹 Deep Learning Models: Use advanced models like BERT for higher prediction accuracy

🔹 Multilingual Support: Extend the model to support multiple languages

🔹 Social Media Integration: Enable real-time emotion predictions from social media or text streams

🔹 User Feedback Loop: Collect feedback from users to continuously improve the model


