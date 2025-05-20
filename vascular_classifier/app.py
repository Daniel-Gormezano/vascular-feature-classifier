#Importing the necessary libraries.
import io
import streamlit as st
import pandas as pd
from vascular_classifier.model_utils import predict_batch

#Set page configuration and hide the default UI.
st.set_page_config(page_title = "Vascular Condition Classifier",
                   page_icon = "🫀", layout = "wide")
st.markdown("""<style> #MainMenu {visibility: hidden;} footer {visibility: hidden;}.block-container {padding-top: 2rem;} h1 {color: #E91E63; font-size: 2.8rem;}
    </style> """, unsafe_allow_html = True)

#Adding a main title and caption.
st.title("🫀 Vascular Condition Classifier 🫀")
st.caption("Upload vascular image metadata and get predictions with confidence scores.")

#Adding a sidebar for file upload.
with st.sidebar:
    st.header("Upload Patient Metadata")
    uploaded_file = st.file_uploader("Choose a CSV file", type = "csv")

#Loading and preprocessing the uploaded file.
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    df.columns = df.columns.str.replace('<','_', regex = False).str.replace('>','_', regex = False)
    orig = "Vascular class(0=no, 1=Hyalinosis, 2=Fibrosis, 3=Hyalinosis+Fibrosis)"
    if orig in df.columns:
        df = df.rename(columns = {orig: "Actual Class"})
        df["Actual Class"] = df["Actual Class"].astype(int)
    
    #Creating the preview and prediction tabs.
    tab1, tab2 = st.tabs(["📄 Preview Data", "📈 Predictions"])
    with tab1:
        st.dataframe(df.head())

    #Generating predictions and rounding each confidence score to 3 decimal places.
    with tab2:
        if st.button("Run Predictions"):
            with st.spinner("Running..."):
                results = predict_batch(df)
                for c in results.select_dtypes("float"):
                    results[c] = results[c].round(3)

                if "Actual Class" in df.columns:
                    results["Actual Class"] = df["Actual Class"].values

                #Define styling functions.
                def _highlight_mismatch(row):
                    return ["background-color: #D32F2F; color: white;"
                        if (col=="Predicted Class" and row["Predicted Class"] != row["Actual Class"])
                        else ""
                        for col in row.index]
                    
                def _highlight_conf(v):
                    if   v >= 0.95: return "background-color: #388E3C; color: white;"
                    elif v >= 0.60: return "background-color: #FBC02D; color: black;"
                    else:           return "background-color: #D32F2F; color: white;"

                #Applying the styling to the results.
                styler = results.style.format(precision = 2)
                if "Actual Class" in results.columns:
                    styler = styler.apply(_highlight_mismatch, axis = 1)
                if "Confidence Score" in results.columns:
                    styler = styler.applymap(_highlight_conf, subset = ["Confidence Score"])

                st.subheader("Predictions:")
                st.dataframe(styler, use_container_width=True)

                #Exporting the styled results to Excel.
                towrite = io.BytesIO()
                with pd.ExcelWriter(towrite, engine = "openpyxl") as writer:
                    styler.to_excel(writer, sheet_name = "Predictions", index = False)
                towrite.seek(0)

                st.download_button("📥 Download Predictions (Excel)", data = towrite, file_name = "vascular_predictions.xlsx", 
                                   mime = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
