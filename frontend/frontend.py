# frontend.py

import streamlit as st
import requests

# ---------------- CONFIG ----------------
API_URL = "https://employee-attrition-ml-system.onrender.com/predict"
"

st.set_page_config(
    page_title="Employee Attrition Predictor",
    layout="centered"
)

st.title("👨‍💼 Employee Attrition Prediction")
st.write(
    "This tool predicts the likelihood of an employee leaving the organization "
    "based on job, compensation, and satisfaction factors."
)

st.divider()

# ---------------- INPUT FORM ----------------
with st.form("attrition_form"):

    st.subheader("🧾 Employee Information")

    Age = st.number_input("Age", min_value=18, max_value=65, value=30)

    Gender = st.selectbox("Gender", ["Male", "Female"])

    MaritalStatus = st.selectbox(
        "Marital Status", ["Single", "Married", "Divorced"]
    )

    Department = st.selectbox(
        "Department",
        ["Sales", "Research & Development", "Human Resources"]
    )

    JobRole = st.selectbox(
        "Job Role",
        [
            "Sales Executive", "Research Scientist", "Laboratory Technician",
            "Manufacturing Director", "Healthcare Representative",
            "Manager", "Sales Representative", "Research Director",
            "Human Resources"
        ]
    )

    Education = st.slider("Education Level (1–5)", 1, 5, 3)

    EducationField = st.selectbox(
        "Education Field",
        ["Life Sciences", "Medical", "Marketing",
         "Technical Degree", "Human Resources", "Other"]
    )

    st.subheader("💼 Work Conditions")

    OverTime = st.selectbox("OverTime", ["Yes", "No"])

    WorkLifeBalance = st.slider("Work Life Balance (1–4)", 1, 4, 3)
    JobSatisfaction = st.slider("Job Satisfaction (1–4)", 1, 4, 3)
    EnvironmentSatisfaction = st.slider("Environment Satisfaction (1–4)", 1, 4, 3)
    JobInvolvement = st.slider("Job Involvement (1–4)", 1, 4, 3)

    st.subheader("💰 Experience & Compensation")

    MonthlyIncome = st.number_input(
        "Monthly Income", min_value=1000, value=6000, step=500
    )

    YearsAtCompany = st.number_input(
        "Years at Company", min_value=0, value=5
    )

    TotalWorkingYears = st.number_input(
        "Total Working Years", min_value=0, value=8
    )

    JobLevel = st.slider("Job Level (1–5)", 1, 5, 2)
    StockOptionLevel = st.slider("Stock Option Level (0–3)", 0, 3, 1)

    submitted = st.form_submit_button("🔍 Predict Attrition")

# ---------------- API CALL ----------------
if submitted:

    payload = {
        "Age": Age,
        "Gender": Gender,
        "MaritalStatus": MaritalStatus,
        "Department": Department,
        "JobRole": JobRole,
        "Education": Education,
        "EducationField": EducationField,
        "OverTime": OverTime,
        "WorkLifeBalance": WorkLifeBalance,
        "JobSatisfaction": JobSatisfaction,
        "EnvironmentSatisfaction": EnvironmentSatisfaction,
        "JobInvolvement": JobInvolvement,
        "MonthlyIncome": MonthlyIncome,
        "YearsAtCompany": YearsAtCompany,
        "TotalWorkingYears": TotalWorkingYears,
        "JobLevel": JobLevel,
        "StockOptionLevel": StockOptionLevel
    }

    with st.spinner("Predicting attrition risk..."):
        try:
            response = requests.post(API_URL, json=payload, timeout=10)

            if response.status_code == 200:
                result = response.json()["predicted as"]

                st.success("Prediction Successful")

                st.metric(
                    label="Attrition Prediction",
                    value=result["predicted_category"]
                )

                st.metric(
                    label="Confidence",
                    value=f"{result['confidence'] * 100:.2f}%"
                )

                st.subheader("📊 Class Probabilities")
                st.json(result["class_probabilities"])

            else:
                st.error(f"API Error: {response.text}")

        except Exception as e:
            st.error(f"Failed to connect to API: {e}")
