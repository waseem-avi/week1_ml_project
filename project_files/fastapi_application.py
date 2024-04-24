from core.model.input_features import FeatureInput

from fastapi import FastAPI, Form
from typing import List




# Create FastAPI instance
app = FastAPI()

# Define a sample endpoint
@app.get("/")
async def read_root():
    return {"message": "Welcome to your FastAPI application!"}

# Define the sub-categories for each categorical feature
experience_levels = ['SE', 'MI', 'EN', 'EX']
employment_types = ['FT', 'CT', 'FL', 'PT']
job_titles = [
    'Principal Data Scientist', 'ML Engineer', 'Data Scientist', 'Applied Scientist',
    'Data Analyst', 'Data Modeler', 'Research Engineer', 'Analytics Engineer',
    'Business Intelligence Engineer', 'Machine Learning Engineer', 'Data Strategist',
    'Data Engineer', 'Computer Vision Engineer', 'Data Quality Analyst',
    'Compliance Data Analyst', 'Data Architect', 'Applied Machine Learning Engineer',
    'AI Developer', 'Research Scientist', 'Data Analytics Manager',
    'Business Data Analyst', 'Applied Data Scientist', 'Staff Data Analyst',
    'ETL Engineer', 'Data DevOps Engineer', 'Head of Data', 'Data Science Manager',
    'Data Manager', 'Machine Learning Researcher', 'Big Data Engineer',
    'Data Specialist', 'Lead Data Analyst', 'BI Data Engineer',
    'Director of Data Science', 'Machine Learning Scientist', 'MLOps Engineer',
    'AI Scientist', 'Autonomous Vehicle Technician', 'Applied Machine Learning Scientist',
    'Lead Data Scientist', 'Cloud Database Engineer', 'Financial Data Analyst',
    'Data Infrastructure Engineer', 'Software Data Engineer', 'AI Programmer',
    'Data Operations Engineer', 'BI Developer', 'Data Science Lead',
    'Deep Learning Researcher', 'BI Analyst', 'Data Science Consultant',
    'Data Analytics Specialist', 'Machine Learning Infrastructure Engineer',
    'BI Data Analyst', 'Head of Data Science', 'Insight Analyst',
    'Deep Learning Engineer', 'Machine Learning Software Engineer',
    'Big Data Architect', 'Product Data Analyst', 'Computer Vision Software Engineer',
    'Azure Data Engineer', 'Marketing Data Engineer', 'Data Analytics Lead',
    'Data Lead', 'Data Science Engineer', 'Machine Learning Research Engineer',
    'NLP Engineer', 'Manager Data Management', 'Machine Learning Developer',
    '3D Computer Vision Researcher', 'Principal Machine Learning Engineer',
    'Data Analytics Engineer', 'Data Analytics Consultant', 'Data Management Specialist',
    'Data Science Tech Lead', 'Data Scientist Lead', 'Cloud Data Engineer',
    'Data Operations Analyst', 'Marketing Data Analyst', 'Power BI Developer',
    'Product Data Scientist', 'Principal Data Architect', 'Machine Learning Manager',
    'Lead Machine Learning Engineer', 'ETL Developer', 'Cloud Data Architect',
    'Lead Data Engineer', 'Head of Machine Learning', 'Principal Data Analyst',
    'Principal Data Engineer', 'Staff Data Scientist', 'Finance Data Analyst'
]  # Add all job titles
salary_currencies = ['USD', 'EUR', 'GBP', 'INR', 'JPY', 'AUD', 'CAD', 'CHF', 'CNY', 'SEK']  # Add all currencies
employee_residences = ['US', 'UK', 'India', 'Germany', 'France', 'Australia', 'Canada', 'China', 'Japan']  # Add all countries
company_locations = ['New York', 'London', 'Bangalore', 'Berlin', 'Paris', 'Sydney', 'Toronto', 'Beijing', 'Tokyo']  # Add all locations
company_sizes = ['L', 'S', 'M']  # Large, Small, Medium


# POST endpoint to handle form submission
@app.post("/predict-salary/")
async def predict_salary( 
    
    experience_level: str = Form(..., title="Experience Level", description="Select your experience level", enum=experience_levels),
    employment_type: str = Form(..., title="Employment Type", description="Select your employment type", enum=employment_types),
    job_title: str = Form(..., title="Job Title", description="Select your job title", enum=job_titles),
    salary_currency: str = Form(..., title="Salary Currency", description="Select your salary currency", enum=salary_currencies),
    employee_residence: str = Form(..., title="Employee Residence", description="Select your employee residence", enum=employee_residences),
    company_location: str = Form(..., title="Company Location", description="Select your company location", enum=company_locations),
    company_size: str = Form(..., title="Company Size", description="Select your company size", enum=company_sizes)
):
    print("predicted")
    return {"predicted_salary": "tiweeentiii rupees"}



# Run the FastAPI application with uvicorn server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)