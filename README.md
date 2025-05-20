# Vascular Feature Classifier

<a id="readme-top"></a>

This project is a Streamlit-powered Python library that classifies vascular conditions (hyalinosis, fibrosis, and combined) based on artery metadata using a calibrated XGBoost model.

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

Diagnosing vascular damage visually from histology or biopsy is labor-intensive and has considerable inter-observer variability. This metadata-driven classifier, the **Vascular Feature Classifier**, allows researchers to upload quantitative vascular image metadata (CSV) and receive multiclass predictions (no lesion, hyalinosis, fibrosis, and hyalinosis + fibrosis) along with confidence scores and per-class probabilities. It uses a pre-trained ensemble model (`xgb_model.pkl`) with data standardization and a consistent feature set.

This tool streamlines the classification of minority vascular conditions by leveraging sample weighting and hyperparameter-tuned XGBoost to achieve the best tradeoff among overall accuracy and minority-class recall, as measured by AUC and F1 scores.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Features

* **Batch predictions**: Upload a CSV of patient metadata and get predictions for all rows.
* **Per-sample confidence**: Display full probability vector and highlight confidence levels.
* **Error highlighting**: Automatically highlights misclassified rows.
* **Downloadable results with Highlighting**: Export predictions as a xslx file with conditional highlighting.
* **Lightweight UI**: Streamlit-based program with minimal dependencies.

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
   git clone https://github.com/Daniel-Gormezano/vascular-feature-classifier.git
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

   * `xgb_model.pkl` (XGBoost model).
   * `scaler.pkl` (StandardScaler fit on training data).
2. **Run the Streamlit app in your terminal**

   ```bash
   streamlit run app.py
   ```
3. **Upload** your CSV file via the sidebar.
4. **View & download** the prediction table.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Model & Metrics

* **Algorithm**: XGBoost classifier.
* **Features**: 376 metadata columns, which include intensity, texture, area, spatial distances, and more.
* **Preprocessing**: Missing values replaced by column means, and features were standardized using StandardScaler.
* **Handling of Class Imbalance**: Sample weighting was introduced for classes 2 (fibrosis) and 3 (hyalinosis + fibrosis).
* **Conditional Highlighting**: >= 0.95 confidence is Green, 0.6 >= confidence is Yellow, < 0.6 confidence is Red.
* **Metrics**:

  * **Weighted AUC**: 0.9968
  * **Macro AUC**: 0.9949
  * **Weighted F1 Score**: 0.9777
  * **Macro F1 Score**: 0.8555

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Project Structure

```
├── LICENSE              #Licensing information
├── README.md            #Project documentation
├── requirements.txt     #Python dependencies
├── setup.py             #Package install script
└── vascular_classifier  #Main Python package
    ├── __init__.py      #Package initializer
    ├── app.py           #Streamlit UI entrypoint
    ├── model_utils.py   #Prediction and preprocessing library
    └── assets           #Serialized model and metadata
        ├── scaler.pkl       #Saved StandardScaler object
        └── xgb_model.pkl    #Saved XGBoost model

```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Future Improvements

* **Improving minority class accuracy** through deeper hyperparameter tuning (XGBoost and class weighting led to substantial improvements).
* **Expanding to multi-omics integration algorithms** (transcriptomics, proteomics).
* **Implementing efficient vessel segmentation** through computer vision networks to improve feature extraction and vessel segmentation.

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

* **LinkedIn**: [Daniel Gormezano](https://www.linkedin.com/in/dgormezano/)
* **Email**: [dangorme@gmail.com](mailto:dangorme@gmail.com)
* **GitHub**: [Daniel‐Gormezano](https://github.com/dgormezano)
* **Project Link**: [https://github.com/Daniel-Gormezano/vascular-feature-classifier](https://github.com/Daniel-Gormezano/vascular-feature-classifier)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Acknowledgements

I sincerely thank Dr. Yuankai Huo for his unwavering support and enthusiasm. His expertise helped me define the project scope, make critical methodological decisions, and positively influence my educational path. His encouragement was a constant source of inspiration throughout this journey!

I am deeply grateful for my co-mentor Yuechen Yang ([GitHub](https://github.com/yuechen-yang)), whose patient mentorship guided me through every aspect of this project, from understanding the data retrieval process and preprocessing code to presenting my findings and discussing future directions. She consistently made herself available, offered invaluable career advice, and played a pivotal role in my growth as a data analyst!

<p align="right">(<a href="#readme-top">back to top</a>)</p>


