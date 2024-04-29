import pickle
with open('src/car_price_prediction/datafiles/random_forest_regression_model.pkl', 'rb') as f:
    model = pickle.load(f)