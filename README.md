# TV Show & Movie Classification App

**Project Overview**

This project is an end-to-end Machine Learning system that classifies TV shows and movies based on their features.
It covers the full ML lifecycle — from data exploration and feature engineering to model training, experiment tracking, deployment, and interactive visualization.

The goal was to design a scalable and reproducible ML pipeline that could be deployed as a real-world application.

**Features**

**Data Engineering & Exploration**

- Normalized dataset design (3NF).

- SQL queries to load structured data into Pandas.

- Extensive EDA with profiling, correlation analysis, and feature cleanup.

**Model Development & Experimentation**

- Built preprocessing pipelines (scaling, encoding, transformations).

- Trained multiple models: Logistic Regression, Ridge, Random Forest, XGBoost.

- Feature selection (correlation threshold, variance threshold, importance-based).

- Dimensionality reduction with PCA (scree plots for component selection).

- Logged experiments, metrics, and parameters using MLflow + DagsHub.

**Deployment**

- Final model saved with joblib.

- Developed a FastAPI application to serve predictions.

- Containerized with Docker and pushed to Docker Hub.

- Deployed to a cloud platform for scalable inference.

**Visualization & User Interaction**

- Built a Streamlit app for real-time classification of TV shows/movies.

- Integrated API predictions into the frontend.

**Tech Stack**

**Languages & Libraries:** Python, Pandas, NumPy, Scikit-learn, XGBoost, Matplotlib, Seaborn

**Experiment Tracking:** MLflow, DagsHub

**Deployment:** FastAPI, Docker, Cloud (e.g., AWS/Heroku)

**Frontend:** Streamlit

**Database & Queries:** PostgreSQL, SQL

**Repository Structure**

├── notebooks/            # EDA, feature engineering, experiments

├── src/                  # Core ML pipeline and model scripts

├── api/                  # FastAPI app

├── frontend/             # Streamlit app

├── docker/               # Dockerfiles and configs

├── requirements.txt      # Dependencies

└── README.md             # Project 


**How to Run Locally**

**Clone the repo:**

git clone https://github.com/nivesharath/tv-show-app.git

cd tv-show-app


**Install dependencies:**

pip install -r requirements.txt


**Run the FastAPI service:**

uvicorn api.main:app --reload


**Run the Streamlit app:**

streamlit run frontend/app.py

**Results**

- Compared multiple models across F1-score, Precision, Recall.

- Feature engineering and selection significantly improved performance.

- Final deployed model achieved high classification accuracy (update with your best metric if available).

**Future Improvements**

- Incorporate additional metadata (e.g., genres, ratings).

- Extend deployment with CI/CD pipelines.

Optimize API for real-time streaming classification.

📹 Demo

JupyterBook Project Site

Recorded video walkthrough explaining dataset, ML experiments, and deployment.
