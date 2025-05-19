# Vascular Feature Classifier

<a id="readme-top"></a>

A Streamlit-powered Python library and web app for classifying renal vascular conditions from quantitative pathomics metadata.

---

## Table of Contents

1. [About The Project](#about-the-project)
2. [Features](#features)
3. [Built With](#built-with)
4. [Getting Started](#getting-started)

   * [Prerequisites](#prerequisites)
   * [Installation](#installation)
5. [Usage](#usage)
6. [Model & Metrics](#model--metrics)
7. [Project Structure](#project-structure)
8. [Future Improvements](#future-improvements)
9. [Contributing](#contributing)
10. [License](#license)
11. [Contact](#contact)

---

## About The Project

The **Vascular Feature Classifier** allows researchers to upload quantitative vascular image metadata (CSV) and receive multiclass predictions (no lesion, hyalinosis, fibrosis, hyalinosis + fibrosis) along with confidence scores and per-class probabilities. It uses a pre-trained ensemble model (`rf_model.pkl`) with data standardization and a consistent feature set.

This tool streamlines classification of minority vascular conditions by leveraging sample weighting, hyperparameter-tuned XGBoost, and a lightweight Streamlit interface.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Features

* **Batch predictions**: Upload a CSV, get predictions for all rows
* **Per-class confidence**: Display full probability vector and highlight confidence levels
* **Error highlighting**: Automatically mark misclassified rows
* **Downloadable results**: Export predictions as CSV
* **Lightweight UI**: Streamlit-based, minimal dependencies

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Built With

* [Python 3.8+](https://www.python.org/)
* [Streamlit](https://streamlit.io/)
* [XGBoost](https://xgboost.readthedocs.io/)
* [scikit-learn](https://scikit-learn.org/)
* [pandas](https://pandas.pydata.org/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Getting Started

Follow these steps to get a local copy running.

### Prerequisites

* Python 3.8 or higher
* `pip` package installer

### Installation

1. **Clone the repo**

   ```bash
   git clone https://github.com/<YourUser>/vascular-feature-classifier.git
   cd vascular-feature-classifier
   ```
2. **Create & activate a virtual environment (optional but recommended)**

   ```bash
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate     # Windows
   ```
3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Usage

1. **Ensure assets** folder contains:

   * `rf_model.pkl` (trained Random Forest or XGBoost model)
   * `scaler.pkl` (StandardScaler fit on training data)
   * `feature_list.txt` (ordered list of feature column names)
2. **Run the Streamlit app**

   ```bash
   streamlit run app.py
   ```
3. **Upload** your CSV file via the sidebar
4. **View & download** the prediction table

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Model & Metrics

* **Model**: XGBoost with sample weighting to emphasize minority class (hyalinosis + fibrosis)
* **Preprocessing**: Missing values replaced by column means, features standardized
* **Metrics**:

  * **Weighted & Macro F1-score**
  * **Weighted & Macro AUC (one-vs-rest)**
  * **Confusion matrix** across stratified 5-fold CV

**Performance Highlights:**

* Macro F1 improved from \~0.70 (raw RF) to \~0.83 (weighted XGBoost)
* Macro AUC up to \~0.996 with hyperparameter tuning and sample weights

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Project Structure

```
├── app.py               # Streamlit UI entrypoint
├── model_utils.py       # Prediction & preprocessing library
├── assets/              # Serialized model & metadata
│   ├── rf_model.pkl
│   ├── scaler.pkl
│   └── feature_list.txt
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Future Improvements

* Integrate SMOTE/ADASYN for synthetic minority oversampling
* Add model interpretability (SHAP or LIME)
* Expand to multi-omics integration (transcriptomics, proteomics)
* Develop desktop GUI wrapper (PyQT or Electron)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Contributing

1. Fork the repo
2. Create a new branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m 'Add feature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Contact

Daniel Gormezano - [LinkedIn - Daniel Gormezano]([https://twitter.com/YourHandle](https://www.linkedin.com/in/dgormezano/)) - [dangorme@gmail.com](mailto:dangorme@gmail.com)

Project Link: [https://github.com/Daniel-Gormezano/vascular-feature-classifier](https://github.com/Daniel-Gormezano/vascular-feature-classifier)

