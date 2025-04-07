from fastapi import FastAPI, HTTPException, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import pickle
import numpy as np
import pandas as pd
from API_Files.Schema import InputFeatures

# Load the saved model and preprocessor
with open("best_model_and_preprocessor.pkl", "rb") as f:
    model = pickle.load(f)

# Initialize FastAPI app
app = FastAPI()

# Template config
templates = Jinja2Templates(directory="templates")

# Route for Home Page
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

# Route for Prediction Form
@app.get("/prediction", response_class=HTMLResponse)
async def form_get(request: Request):
    return templates.TemplateResponse("form.html", {"request": request, "prediction": None})

@app.post("/prediction", response_class=HTMLResponse)
async def form_post(
    request: Request,
    age: float = Form(...),
    bmi: float = Form(...),
    children: int = Form(...),
    sex: str = Form(...),
    smoker: str = Form(...),
    region: str = Form(...)
):
    try:
        # Create InputFeatures instance
        features = InputFeatures(
            age=age,
            bmi=bmi,
            children=children,
            sex=sex,
            smoker=smoker,
            region=region
        )

        # Convert to dict/DataFrame
        input_df = pd.DataFrame([features.model_dump()])

        # Make prediction
        prediction = model.predict(input_df)[0]

        return templates.TemplateResponse("form.html", {
            "request": request,
            "prediction": prediction
        })

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
