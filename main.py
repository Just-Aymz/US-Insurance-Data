from fastapi import FastAPI, HTTPException
import pickle
import numpy as np
import pandas as pd
from Schema import InputFeatures

# Load the saved model and preprocessor
with open("best_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("preprocessor.pkl", "rb") as f:
    preprocessor = pickle.load(f)

# Initialize FastAPI app
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to the Machine Learning API"}

@app.post("/predict")
def predict(data: InputFeatures):
    try:
        # Convert Pydantic model to dictionary
        input_dict = dict(data)

        # Convert to DataFrame
        input_df = pd.DataFrame([input_dict])

        # Apply transformations
        X_transformed = preprocessor.transform(input_df)

        # Make a prediction
        prediction = model.predict(X_transformed)

        return {"prediction": prediction.tolist()}
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
