import pickle

def saveModel(model_pipeline,filename):
    # Save the model to a file
    pickle.dump(model_pipeline, open(filename, 'wb'))

