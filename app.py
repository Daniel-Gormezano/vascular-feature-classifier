#Importing the necessary libraries.
import streamlit as st
import pandas as pd
from model_utils import predict_batch

#Changing the page configuration and adding stylistic features.
st.set_page_config(page_title = "Vascular Condition Classifier",
                   page_icon = "🫀", layout = "wide")

st.markdown("""<style> #MainMenu {visibility: hidden;} footer {visibility: hidden;} .block-container {padding-top: 2rem;} h1 {color: #E91E63; font-size: 2.8rem;}
    </style> """, unsafe_allow_html=True)

#Adding a title and caption to the page.
st.title("🫀 Vascular Condition Classifier 🫀")
st.caption("Upload vascular image metadata and get predictions with confidence scores.")

#Adding a sidbar for the user to upload their patient metadata. 
with st.sidebar:
    st.header("Upload Patient Metadata")
    uploaded_file = st.file_uploader("Choose a CSV file", type = "csv")

#Changing the logic to make cells be highlighted depending if the actual class matches the predicted class and how high the confidence score is.
if uploaded_file:
    df = pd.read_csv(uploaded_file)

    #Renaming the target class.
    orig = "Vascular class(0=no, 1=Hyalinosis, 2=Fibrosis, 3=Hyalinosis+Fibrosis)"
    if orig in df.columns:
        df = df.rename(columns = {orig: "Actual Class"})
        df["Actual Class"] = df["Actual Class"].astype(int)

    #Adding icons to the tabs of the page.
    tab1, tab2 = st.tabs(["📄 Preview Data", "📈 Predictions"])
    with tab1:
        st.dataframe(df.head())

    with tab2:
        if st.button("Run Predictions"):
            with st.spinner("Running..."):

                #The raw predictions of the model.
                results = predict_batch(df)

                #Rounding the confidence scores to 2 decimal places.
                for c in results.select_dtypes("float"):
                    results[c] = results[c].round(2)

                #Attaching the actual values to the columns.
                if "Actual Class" in df.columns:
                    results["Actual Class"] = df["Actual Class"].values

                #Stylistic functions.
                def _highlight_mismatch(row):
                    return ["background-color: #D32F2F; color: white;"
                          if (col=="Predicted Class" and row["Predicted Class"]!=row["Actual Class"])
                        else ""
                        for col in row.index]

                #Adding the colors of the cells depending on confidence scores.
                def _highlight_conf(v):
                    if   v >= 0.95:  return "background-color: #388E3C; color: white;"  
                    elif v >= 0.60:  return "background-color: #FBC02D; color: black;"  
                    else:            return "background-color: #D32F2F; color: white;"  

                #Adding styles and formatting.
                styler = results.style.format(precision = 2)

                #Adding row-wise mismatch.
                if "Actual Class" in results.columns:
                    styler = styler.apply(_highlight_mismatch, axis = 1)

                #Confidence coloring.
                if "Confidence Score" in results.columns:
                    styler = styler.applymap(_highlight_conf, subset = ["Confidence Score"])

                st.subheader("Predictions:")
                st.dataframe(styler, use_container_width = True)

                #Allowing the user to download the predicted classes and confidence scores.
                st.download_button("📥 Download Predictions", data = results.to_csv(index = False), file_name = "vascular_predictions.csv", mime = "text/csv")