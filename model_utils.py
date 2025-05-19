
import pandas as pd
import joblib

# Load model, scaler, and feature list
model = joblib.load("assets/rf_model.pkl")
scaler = joblib.load("assets/scaler.pkl")
with open("assets/feature_list.txt") as f:
    feature_list = f.read().splitlines()

def preprocess_input(input_df):
    # Add missing columns with 0 (or replace with column mean if known)
    for col in feature_list:
        if col not in input_df.columns:
            input_df[col] = 0

    # Reorder columns
    input_df = input_df[feature_list]

    # Fill NaNs
    input_df = input_df.fillna(input_df.mean())

    # Scale
    scaled = scaler.transform(input_df)
    return pd.DataFrame(scaled, columns=feature_list)

def predict_class(input_df):
    processed = preprocess_input(input_df)
    prediction = model.predict(processed)
    return prediction

def predict_batch(input_df):
    processed = preprocess_input(input_df)
    predictions = model.predict(processed)
    confidences = model.predict_proba(processed)
    
    # Build dataframe with predicted class and max confidence
    results = pd.DataFrame({
        "Predicted Class": predictions,
        "Confidence Score": confidences.max(axis=1)
    })
    
    # Add class-specific probabilities
    class_prob_df = pd.DataFrame(confidences, columns=[f"Prob_Class_{c}" for c in model.classes_])
    results = pd.concat([results, class_prob_df], axis=1)
    
    return results
