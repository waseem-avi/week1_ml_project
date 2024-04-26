import pickle

# Load the encoder from the pickle file
with open('project_files/datafiles/encoder.pkl', 'rb') as file:
    encoder = pickle.load(file)
# Load the model from the pickle file
with open('project_files/datafiles/LinearRegression.pkl', 'rb') as file:
    model = pickle.load(file)
   
