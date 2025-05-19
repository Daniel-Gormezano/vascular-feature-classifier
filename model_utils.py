import pandas as pd
import joblib

#Loading the model, scaler, and features list.
model = joblib.load("assets/rf_model.pkl")
scaler = joblib.load("assets/scaler.pkl")
with open("assets/feature_list.txt") as f:
    feature_list = f.read().splitlines()

def preprocess_input(input_df):
    #Replace the NA values with the column mean.
    for col in feature_list:
        if col not in input_df.columns:
            input_df[col] = 0

    #Reordering the columns.
    input_df = input_df[feature_list]
    input_df = input_df.fillna(input_df.mean())

    #Scaling the columns.
    scaled = scaler.transform(input_df)
    return pd.DataFrame(scaled, columns = feature_list)

#Function to predict the class of the sample.
def predict_class(input_df):
    processed = preprocess_input(input_df)
    prediction = model.predict(processed)
    return prediction

#Function determine the confidence in the model's predictions.
def predict_batch(input_df):
    processed = preprocess_input(input_df)
    predictions = model.predict(processed)
    confidences = model.predict_proba(processed)
    
    #Creating a dataframe with predicted class and maximum confidence.
    results = pd.DataFrame({"Predicted Class": predictions, "Confidence Score": confidences.max(axis = 1)})
    
    #Adding class-specific probabilities.
    class_prob_df = pd.DataFrame(confidences, columns = [f"Prob_Class_{c}" for c in model.classes_])
    results = pd.concat([results, class_prob_df], axis = 1)
    
    return results
