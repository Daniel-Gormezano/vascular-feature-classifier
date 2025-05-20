import pandas as pd
import joblib

#Loading the model, scaler, and features list.
model  = joblib.load("assets/xgb_model.pkl")
scaler = joblib.load("assets/scaler.pkl")
feature_list = model.get_booster().feature_names

def preprocess_input(input_df):
    #Replacing the column names with characters that allow the XGBoost to be run. 
    input_df.columns = (input_df.columns.str.replace("<", "_", regex = False).str.replace(">", "_", regex = False).str.strip())

    #Ensuring every feature is present.
    for col in feature_list:
        if col not in input_df.columns:
            input_df[col] = 0

    #Replacing NA values with the column means.
    input_df = input_df[feature_list].fillna(input_df.mean())

    #Scaling the columns.
    scaled_array = scaler.transform(input_df.values)

    #Returning the dataframe with the proper column names.
    return pd.DataFrame(scaled_array, columns = feature_list)

#Function to predict the class of the sample.
def predict_class(input_df):
    df_scaled = preprocess_input(input_df)
    return model.predict(df_scaled)

#Function determine the confidence in the model's predictions.
def predict_batch(input_df):
    df_scaled = preprocess_input(input_df)
    preds = model.predict(df_scaled)
    conf_matrix = model.predict_proba(df_scaled)

    #Creating a dataframe with predicted class and maximum confidence.
    results = pd.DataFrame({"Predicted Class": preds, "Confidence Score": conf_matrix.max(axis = 1)})
    probs = pd.DataFrame(conf_matrix, columns = [f"Prob_Class_{c}" for c in model.classes_])
    return pd.concat([results, probs], axis = 1)