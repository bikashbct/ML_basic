import streamlit as st 
import joblib



model = joblib.load("model.joblib")
st.title("News Category Prediciton")
st.markdown ("Enter News here: ")


input_text = st.text_area(
    label = "" , max_chars = 10000, height = 300
)

if st.button("Predict Category"):
    prediction = model.predict([input_text[0]])
    st.sucess(f"Predicted category si {prediction}")
