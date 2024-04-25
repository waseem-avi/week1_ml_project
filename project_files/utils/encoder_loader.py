import pickle

# Load the model from the pickle file
with open('project_files/Datafiles/encoder.pkl', 'rb') as file:
    encoder = pickle.load(file)
    print(encoder)
