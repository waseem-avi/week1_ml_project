import numpy as np
def transformer (Present_Price, Kms_Driven, Owner,  Fuel_Type_Petrol, Seller_Type_Individual, Transmission_Manual, Year):
    Kms_Driven2 = np.log(Kms_Driven)
    Fuel_Type_Diesel = 1 if Fuel_Type_Petrol == 'Petrol' else 0
    Seller_Type_Individual = 1 if Seller_Type_Individual == 'Individual' else 0
    Transmission_Manual = 1 if Transmission_Manual == 'Manual' else 0
    Year = 2024 - Year
    return [Present_Price, Kms_Driven2, Owner, Year, Fuel_Type_Diesel, 1 - Fuel_Type_Diesel, Seller_Type_Individual, Transmission_Manual]