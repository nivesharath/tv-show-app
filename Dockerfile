
# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code and model into the container
COPY app.py .
COPY final_model.joblib .

# Expose port 8080 for the API (Google Cloud Run expects this)
EXPOSE 8000

# Command to run the application using uvicorn
CMD ["sh", "-c", "uvicorn app:app --host 0.0.0.0 --port $PORT"]
