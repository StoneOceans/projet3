from pydantic import BaseModel

class EmployeeInput(BaseModel):
    age: int
    monthly_income: float
    years_at_company: int
    job_satisfaction: int
    work_life_balance: int
    overtime: int

class PredictionOutput(BaseModel):
    prediction: int
    probability: float