from typing import Annotated, List,Optional,Literal
from pydantic import BaseModel,Field
import pandas as pd

class InputData(BaseModel):
    Age:Annotated[int,Field(...,description="Age of the employee",examples=[25], ge=18, lt=120)]
    Gender:Annotated[Literal['Male','Female'],Field(...,description="Gender of the employee")]  
    MaritalStatus:Annotated[Literal['Single','Married','Divorced'],Field(...,description="Marital status of the employee")]
    Department:Annotated[Literal['Sales','Research & Development','Human Resources'],Field(...,description="Department of the employee")]
    JobRole:Annotated[Literal['Sales Executive','Research Scientist','Laboratory Technician','Manufacturing Director','Healthcare Representative','Manager','Sales Representative','Research Director','Human Resources'],Field(...,description="Job role of the employee")]    
    Education:Annotated[int,Field(...,description='Education level of Employee :-[1,2,3,4,5]',examples=[1],ge=1,le=5)]
    EducationField:Annotated[Literal['Life Sciences','Medical','Marketing','Technical Degree','Human Resources','Other'],Field(...,description="Field of education of the employee")]
    OverTime:Annotated[Literal['Yes','No'],Field(...,description="Whether the employee works overtime or not")]
    WorkLifeBalance:Annotated[int,Field(...,description="Work life balance level on a scale of 1-4",examples=[3],ge=1,le=4)]
    JobSatisfaction:Annotated[int,Field(...,description="Job satisfaction level on a scale of 1-4",examples=[3],ge=1,le=4)]
    EnvironmentSatisfaction:Optional[Annotated[int,Field(description="Environment satisfaction level on a scale of 1-4",examples=[3],ge=1,le=4)]]
    JobInvolvement:Annotated[int,Field(...,description="Job involvement level on a scale of 1-4",examples=[3],ge=1,le=4)]
    MonthlyIncome:Annotated[int,Field(...,description="Monthly income of the employee",examples=[5000],ge=1000)]
    YearsAtCompany: Annotated[int,Field(...,description="Number of years the employee has been at the company",examples=[5],ge=0)]
    TotalWorkingYears: Annotated[int,Field(...,description="Total number of years the employee has worked",examples=[10],ge=0)]
    JobLevel: Annotated[int,Field(...,description="Job level of the employee on a scale of 1-5",examples=[2],ge=1,le=5)]
    StockOptionLevel: Annotated[int,Field(...,description="Stock option level of the employee on a scale of 0-3",examples=[1],ge=0,le=3)]
