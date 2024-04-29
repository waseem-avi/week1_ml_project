from pydantic import BaseModel

class CarData(BaseModel):
    Year: int
    Present_Price: float
    Kms_Driven: int
    Owner: int
    Fuel_Type_Petrol: str
    Seller_Type_Individual: str
    Transmission_Mannual: str