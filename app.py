from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
import os

# Load the saved classification model
model = joblib.load("final_model.joblib")

# Initialize FastAPI app
app = FastAPI()

# Define input schema for classification requests
class ClassificationInput(BaseModel):
    imdb_score: float
    rotten_tomatoes_score: float
    year: int

# Define output schema for classification responses
class ClassificationOutput(BaseModel):
    predicted_class: str

# Define label mapping (update based on your dataset)
label_mapping = {
    0: "7+",
    1: "13+",
    2: "16+",
    3: "18+"
}

@app.post("/classify", response_model=ClassificationOutput)
def classify(input_data: ClassificationInput):
    # Create a DataFrame from input data
    input_df = pd.DataFrame([{
        "imdb_score": input_data.imdb_score,
        "rotten_tomatoes_score": input_data.rotten_tomatoes_score,
        "combined_score": input_data.imdb_score * input_data.rotten_tomatoes_score,  # Calculate combined_score
        "year": input_data.year
    }])

    # Classify input data
    predicted_class_index = model.predict(input_df)[0]
    
    # Map predicted class index to label
    predicted_class_label = label_mapping.get(predicted_class_index, "Unknown")
    
    return {"predicted_class": predicted_class_label}

# If running directly, enable the server (uncomment for local testing)
if __name__ == "_main_":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))  # Get the PORT from environment
    uvicorn.run(app, host="0.0.0.0", port=port)