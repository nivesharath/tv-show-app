import streamlit as st
import requests

# Streamlit app title
st.title("Movie Classification App")

# Input fields for user data
st.header("Enter Movie Details")
imdb_score = st.number_input("IMDB Score", min_value=0.0, max_value=10.0, value=7.0, step=0.1)
rotten_tomatoes_score = st.number_input("Rotten Tomatoes Score (%)", min_value=0, max_value=100, value=85, step=1)
year = st.number_input("Year", min_value=1900, max_value=2100, value=2022, step=1)

# Backend URL for the FastAPI server
backend_url = "https://fastapi-classification-api-7dc7d4c3c01f.herokuapp.com/classify"

# Submit button
if st.button("Classify"):
    # Prepare the data payload
    payload = {
        "imdb_score": imdb_score,
        "rotten_tomatoes_score": rotten_tomatoes_score,
        "year": year
    }

    # Send a POST request to the FastAPI server
    try:
        response = requests.post(backend_url, json=payload)
        if response.status_code == 200:
            # Extract and display the predicted class
            result = response.json()
            predicted_class = result.get("predicted_class", "Unknown")
            st.success(f"Predicted Classification: {predicted_class}")
        else:
            st.error(f"Error: {response.status_code} - {response.text}")
    except requests.exceptions.RequestException as e:
        st.error(f"Failed to connect to the backend: {e}")
