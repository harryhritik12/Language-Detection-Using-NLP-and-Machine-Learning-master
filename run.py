import streamlit as st
import pickle

# Load the Language Detection Model
def load_model():
    with open('Language-Detection-Using-NLP-and-Machine-Learning-master/lrmodel2.pckl', 'rb') as file:
        model = pickle.load(file)
    return model

# Initialize the app and load the model
st.title("Language Detection App")
st.write("Enter text below to detect its language.")
model = load_model()

# Input text from user
text_input = st.text_area("Text Input", "Type here...")

# Predict button and prediction logic
if st.button("Detect Language"):
    if text_input.strip():
        try:
            # Predict the language
            prediction = model.predict([text_input])[0]
            st.write(f"Detected Language: {prediction}")
        except Exception as e:
            st.write("An error occurred during prediction.")
            st.write(e)
    else:
        st.write("Please enter some text.")
