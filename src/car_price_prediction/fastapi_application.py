from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import HTMLResponse
import pickle
import numpy as np
from pydantic import BaseModel
from sklearn.preprocessing import StandardScaler

app = FastAPI()

class CarData(BaseModel):
    Year: int
    Present_Price: float
    Kms_Driven: int
    Owner: int
    Fuel_Type_Petrol: str
    Seller_Type_Individual: str
    Transmission_Mannual: str

@app.get("/", response_class=HTMLResponse)
async def home():
    return """
    <html>
        <head>
            <title>Car Price Prediction</title>
        </head>
        <body>
            <h1>Car Price Prediction</h1>
            <form action="/predict" method="post" enctype="application/x-www-form-urlencoded">
                <label for="Year">Year:</label><br>
                <input type="text" id="Year" name="Year"><br>
                <label for="Present_Price">Present Price:</label><br>
                <input type="text" id="Present_Price" name="Present_Price"><br>
                <label for="Kms_Driven">Kilometers Driven:</label><br>
                <input type="text" id="Kms_Driven" name="Kms_Driven"><br>
                <label for="Owner">Owner:</label><br>
                <input type="text" id="Owner" name="Owner"><br>
                <label for="Fuel_Type_Petrol">Fuel Type (Petrol/Diesel):</label><br>
                <input type="text" id="Fuel_Type_Petrol" name="Fuel_Type_Petrol"><br>
                <label for="Seller_Type_Individual">Seller Type (Individual/Dealer):</label><br>
                <input type="text" id="Seller_Type_Individual" name="Seller_Type_Individual"><br>
                <label for="Transmission_Mannual">Transmission Type (Manual/Automatic):</label><br>
                <input type="text" id="Transmission_Mannual" name="Transmission_Mannual"><br><br>
                <input type="submit" value="Predict">
            </form>
        </body>
    </html>
    """

@app.post("/predict")
async def predict(
    Year: int = Form(...),
    Present_Price: float = Form(...),
    Kms_Driven: int = Form(...),
    Owner: int = Form(...),
    Fuel_Type_Petrol: str = Form(...),
    Seller_Type_Individual: str = Form(...),
    Transmission_Mannual: str = Form(...)
):
    # Load the model
    model = pickle.load(open('src/car_price_prediction/datafiles/random_forest_regression_model.pkl', 'rb'))

    # Transform input data
    Kms_Driven2 = np.log(Kms_Driven)
    Fuel_Type_Diesel = 1 if Fuel_Type_Petrol == 'Petrol' else 0
    Seller_Type_Individual = 1 if Seller_Type_Individual == 'Individual' else 0
    Transmission_Mannual = 1 if Transmission_Mannual == 'Mannual' else 0
    Year = 2024 - Year

    # Make prediction
    prediction = model.predict([[Present_Price, Kms_Driven2, Owner, Year, Fuel_Type_Diesel, 1 - Fuel_Type_Diesel, Seller_Type_Individual, Transmission_Mannual]])
    output = round(prediction[0], 2)

    # Check for invalid predictions
    if output < 0:
        raise HTTPException(status_code=400, detail="Sorry, you cannot sell this car")

    return {"prediction": output}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)