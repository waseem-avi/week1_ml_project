from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import HTMLResponse

import numpy as np

from models.pydantic_model import CarData
from utils.files_loader import model 
import  utils.input_tranformer 

app = FastAPI()



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
                <label for="Transmission_Manual">Transmission Type (Manual/Automatic):</label><br>
                <input type="text" id="Transmission_Manual" name="Transmission_Manual"><br><br>
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
    Transmission_Manual: str = Form(...)
):
    input_feats= utils.input_tranformer.tranformer (Present_Price, Kms_Driven, Owner,  Fuel_Type_Petrol, Seller_Type_Individual, Transmission_Manual, Year)

   

    # Make prediction
    prediction = model.predict([input_feats])
    output = round(prediction[0], 2)

    # Check for invalid predictions
    if output < 0:
        raise HTTPException(status_code=400, detail="Sorry, you cannot sell this car")

    return {"prediction": output}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)