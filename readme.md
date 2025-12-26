# Employee Attrition Prediction System 🚀

An end-to-end Machine Learning project that predicts employee attrition using a production-ready architecture.

## 🔧 Features
- ML pipeline trained on HR data
- FastAPI backend with Pydantic validation
- Feature assembly layer for schema alignment
- Streamlit interactive frontend
- Health checks and model versioning

## 📊 Model Performance
- Focused on Recall due to class imbalance
- Recall (Attrition = Yes): ~70%
- Evaluated using cross-validation

## 🧠 Tech Stack
Python, Scikit-learn, FastAPI, Pydantic v2, Streamlit, Joblib

## ▶️ How to Run

### Backend
```bash
uvicorn app:app --reload
