from fastapi import FastAPI, HTTPException
import pickle
import numpy as np
import pandas as pd
from Schema import InputFeatures

# Load the saved model and preprocessor
with open("best_model_and_preprocessor.pkl", "rb") as f:
    model = pickle.load(f)

# Initialize FastAPI app
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to the Machine Learning API"}

@app.post("/predict")
def predict(input_data: InputFeatures):
    try:
        # Convert input_data into a dataframe (expected by the model)
        input_df = pd.DataFrame([input_data.dict()])

        print(f"received_data: {input_data.model_dump()}")

        # Make a prediction
        prediction = model.predict(input_df)

        return {"prediction": prediction[0]}
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
