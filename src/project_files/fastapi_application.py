from core.model.input_features import FeatureInput
from utils.files_loader import encoder, model
import mongoengine



from fastapi import FastAPI, Form
from typing import List

from config.v1.database_config import mongo_config

mongoengine.connect(db='salary_data', host = mongo_config.mongo_host)
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
salary_currencies =['EUR', 'USD', 'INR', 'HKD', 'CHF', 'GBP', 'AUD', 'SGD', 'CAD', 'ILS', 'BRL', 'THB', 'PLN', 'HUF', 'CZK', 'DKK', 'JPY', 'MXN', 'TRY', 'CLP']  # Add all currencies
employee_residences = ['ES', 'US', 'CA', 'DE', 'GB', 'NG', 'IN', 'HK', 'PT', 'NL', 'CH', 'CF', 'FR', 'AU',
             'FI', 'UA', 'IE', 'IL', 'GH', 'AT', 'CO', 'SG', 'SE', 'SI', 'MX', 'UZ', 'BR', 'TH',
             'HR', 'PL', 'KW', 'VN', 'CY', 'AR', 'AM', 'BA', 'KE', 'GR', 'MK', 'LV', 'RO', 'PK',
             'IT', 'MA', 'LT', 'BE', 'AS', 'IR', 'HU', 'SK', 'CN', 'CZ', 'CR', 'TR', 'CL', 'PR',
             'DK', 'BO', 'PH', 'DO', 'EG', 'ID', 'AE', 'MY', 'JP', 'EE', 'HN', 'TN', 'RU', 'DZ',
             'IQ', 'BG', 'JE', 'RS', 'NZ', 'MD', 'LU', 'MT']  # Add all countries
company_locations = ['ES', 'US', 'CA', 'DE', 'GB', 'NG', 'IN', 'HK', 'NL', 'CH', 'CF', 'FR', 'FI', 'UA',
             'IE', 'IL', 'GH', 'CO', 'SG', 'AU', 'SE', 'SI', 'MX', 'BR', 'PT', 'RU', 'TH', 'HR',
             'VN', 'EE', 'AM', 'BA', 'KE', 'GR', 'MK', 'LV', 'RO', 'PK', 'IT', 'MA', 'PL', 'AL',
             'AR', 'LT', 'AS', 'CR', 'IR', 'BS', 'HU', 'AT', 'SK', 'CZ', 'TR', 'PR', 'DK', 'BO',
             'PH', 'BE', 'ID', 'EG', 'AE', 'LU', 'MY', 'HN', 'JP', 'DZ', 'IQ', 'CN', 'NZ', 'CL',
             'MD', 'MT']  # Add all locations
company_sizes = ['L', 'S', 'M']  # Large, Small, Medium


# POST endpoint to handle form submission
@app.post("/predict-salary")
async def predict_salary( 
    
    experience_level: str = Form(..., title="Experience Level", description="Select your experience level", enum=experience_levels),
    employment_type: str = Form(..., title="Employment Type", description="Select your employment type", enum=employment_types),
    job_title: str = Form(..., title="Job Title", description="Select your job title", enum=job_titles),
    salary_currency: str = Form(..., title="Salary Currency", description="Select your salary currency", enum=salary_currencies),
    employee_residence: str = Form(..., title="Employee Residence", description="Select your employee residence", enum=employee_residences),
    company_location: str = Form(..., title="Company Location", description="Select your company location", enum=company_locations),
    company_size: str = Form(..., title="Company Size", description="Select your company size", enum=company_sizes)
):
    user_input = list([experience_level,employment_type,job_title,salary_currency,employee_residence,company_location,company_size])
    # print("About to rev-encode")
    # Encode user input using the loaded label encoder
    # encoded_input = encoder.transform(user_input)

    # Perform inference using the trained model
    # predictions = model.predict(encoded_input)

    
    
    return {"predicted_salary": f"76900"}



# # Run the FastAPI application with uvicorn server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)