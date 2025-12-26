from fastapi import FastAPI
import joblib
from pathlib import Path
import pandas as pd
from schema.validate import InputData
from feature_builders import assemble_features,TRAINING_COLUMNS
from fastapi.responses import JSONResponse 
from model.predict import predict_output



app = FastAPI(title="Employee Attrition Predictor")
BASE_DIR = Path(__file__).resolve().parent




MODEL_PATH = BASE_DIR / "model" / "attrition_pred_model.joblib"
ENCODER_PATH = BASE_DIR / "model" / "label_encoder.joblib"

print("MAIN FILE LOADED FROM:", __file__)
print("BASE_DIR:", BASE_DIR)
print("MODEL PATH EXISTS:", MODEL_PATH.exists())

@app.get("/")
def root():
    return {
        "message": "Employee Attrition Prediction API",
        "docs": "/docs",
        "health": "/health"
    }



@app.on_event("startup")
def load_model():
    global model, label_encoder
    model = joblib.load(MODEL_PATH)
    label_encoder = joblib.load(ENCODER_PATH)


@app.get("/health")
def health_check():
    return {'status':"Service is healthy!",
            'Model Version':"1.0.0",
            'API Version':"1.0.0",
            'Model Loaded': model is  not None}




@app.post("/predict")
def predict(data: InputData):
    features = assemble_features(data)
    try:
        result = predict_output(model, label_encoder, features)    
        return JSONResponse(status_code=200,content={"predicted as": result})
    except Exception as e:
        return JSONResponse(status_code=500,content=str(e))
    