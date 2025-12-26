import pandas as pd
from schema.validate import InputData


TRAINING_COLUMNS = ['Age',
 'BusinessTravel',
 'DailyRate',
 'Department',
 'DistanceFromHome',
 'Education',
 'EducationField',
 'EmployeeNumber',
 'EnvironmentSatisfaction',
 'Gender',
 'HourlyRate',
 'JobInvolvement',
 'JobLevel',
 'JobRole',
 'JobSatisfaction',
 'MaritalStatus',
 'MonthlyIncome',
 'MonthlyRate',
 'NumCompaniesWorked',
 'OverTime',
 'PercentSalaryHike',
 'PerformanceRating',
 'RelationshipSatisfaction',
 'StockOptionLevel',
 'TotalWorkingYears',
 'TrainingTimesLastYear',
 'WorkLifeBalance',
 'YearsAtCompany',
 'YearsInCurrentRole',
 'YearsSinceLastPromotion',
 'YearsWithCurrManager']

def assemble_features(inp: InputData) -> dict:
    """
    Builds full feature dictionary expected by the trained pipeline
    """

    features = {}

    # ---------- Direct mappings (user provided) ----------
    features['Age'] = inp.Age
    features['Gender'] = inp.Gender
    features['MaritalStatus'] = inp.MaritalStatus
    features['Department'] = inp.Department
    features['JobRole'] = inp.JobRole
    features['Education'] = inp.Education
    features['EducationField'] = inp.EducationField
    features['OverTime'] = inp.OverTime
    features['WorkLifeBalance'] = inp.WorkLifeBalance
    features['JobSatisfaction'] = inp.JobSatisfaction
    features['EnvironmentSatisfaction'] = inp.EnvironmentSatisfaction
    features['JobInvolvement'] = inp.JobInvolvement
    features['MonthlyIncome'] = inp.MonthlyIncome
    features['YearsAtCompany'] = inp.YearsAtCompany
    features['TotalWorkingYears'] = inp.TotalWorkingYears
    features['JobLevel'] = inp.JobLevel
    features['StockOptionLevel'] = inp.StockOptionLevel

    # ---------- Constants (system-defined) ----------
    features['EmployeeCount'] = 1
    features['EmployeeNumber'] = 0
    features['Over18'] = 'Y'
    features['StandardHours'] = 80

    # ---------- Derived features ----------
    features['YearsInCurrentRole'] = min(inp.YearsAtCompany, 5)
    features['YearsSinceLastPromotion'] = max(inp.YearsAtCompany - 2, 0)
    features['YearsWithCurrManager'] = min(inp.YearsAtCompany, 4)

    # ---------- Defaulted numeric features ----------
    features['DailyRate'] = inp.MonthlyIncome // 30
    features['HourlyRate'] = features['DailyRate'] // 8
    features['MonthlyRate'] = inp.MonthlyIncome
    features['DistanceFromHome'] = 10
    features['NumCompaniesWorked'] = 2
    features['TrainingTimesLastYear'] = 2
    features['PercentSalaryHike'] = 13
    features['PerformanceRating'] = 3
    features['RelationshipSatisfaction'] = 3

    # ---------- Default categorical ----------
    features['BusinessTravel'] = 'Travel_Rarely'

    return features


def to_dataframe(features: dict) -> pd.DataFrame:
    df = pd.DataFrame([features])
    return df[TRAINING_COLUMNS]   # enforces order


def test_assembly_happy_path():
    inp = InputData(
        Age=30,
        Gender='Male',
        MaritalStatus='Single',
        Department='Sales',
        JobRole='Sales Executive',
        Education=3,
        EducationField='Marketing',
        OverTime='Yes',
        WorkLifeBalance=3,
        JobSatisfaction=4,
        EnvironmentSatisfaction=3,
        JobInvolvement=3,
        MonthlyIncome=6000,
        YearsAtCompany=5,
        TotalWorkingYears=8,
        JobLevel=2,
        StockOptionLevel=1
    )

    features = assemble_features(inp)

    # Check count
    assert len(features) == 35

    # Check mandatory columns
    for col in TRAINING_COLUMNS:
        assert col in features


def test_derived_features():
    inp = InputData(
        Age=40,
        Gender='Female',
        MaritalStatus='Married',
        Department='Research & Development',
        JobRole='Research Scientist',
        Education=4,
        EducationField='Life Sciences',
        OverTime='No',
        WorkLifeBalance=2,
        JobSatisfaction=2,
        EnvironmentSatisfaction=2,
        JobInvolvement=2,
        MonthlyIncome=9000,
        YearsAtCompany=10,
        TotalWorkingYears=15,
        JobLevel=3,
        StockOptionLevel=2
    )

    f = assemble_features(inp)

    assert f['YearsInCurrentRole'] == 5          # capped
    assert f['YearsSinceLastPromotion'] == 8     # 10 - 2
    assert f['YearsWithCurrManager'] == 4        # capped

def test_dataframe_schema():
    inp = InputData(
        Age=35,
        Gender='Female',
        MaritalStatus='Divorced',
        Department='Sales',
        JobRole='Manager',
        Education=3,
        EducationField='Marketing',
        OverTime='Yes',
        WorkLifeBalance=3,
        JobSatisfaction=3,
        EnvironmentSatisfaction=3,
        JobInvolvement=3,
        MonthlyIncome=8000,
        YearsAtCompany=6,
        TotalWorkingYears=12,
        JobLevel=3,
        StockOptionLevel=1
    )

    features = assemble_features(inp)
    df = pd.DataFrame([features])[TRAINING_COLUMNS]

    assert list(df.columns) == TRAINING_COLUMNS
    assert df.shape == (1, 35)
