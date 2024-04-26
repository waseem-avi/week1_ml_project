import mongoengine
class SalaryPrediction (mongoengine.Document):
    experience_level=mongoengine.StringField(required=True)
    employment_type=mongoengine.StringField(required=True)
    job_title=mongoengine.StringField(required=True)
    salary_currency=mongoengine.StringField(required=True)
    employee_residence=mongoengine.StringField(required=True)
    company_location=mongoengine.StringField(required=True)
    company_size=mongoengine.StringField(required=True)
    predicted_salary = mongoengine.IntField()