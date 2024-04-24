from pydantic import BaseModel

# Pydantic model for form data
class FeatureInput(BaseModel):
    experience_level: str
    employment_type: str
    job_title: str
    salary_currency: str
    employee_residence: str
    company_location: str
    company_size: str