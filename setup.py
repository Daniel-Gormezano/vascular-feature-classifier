from setuptools import setup, find_packages

setup(name = "vascular-classifier",                  
    version = "0.1.0",
    author = "Daniel Gormezano",
    author_email = "dangorme@gmail.com",
    description = "Pathomics and transcriptomics vascular classifier with Streamlit UI",
    long_description = open("README.md", encoding = "utf-8").read(),
    license = "MIT",
    packages = find_packages(),                    
    include_package_data = True,                  
    install_requires = ["streamlit", "pandas", "numpy", "matplotlib", "scikit-learn", "xgboost", "openpyxl", "joblib"],
    entry_points = {"console_scripts": ["vascular-classifier-app = vascular_classifier.app:main",],},
    package_data = {"vascular_classifier": ["assets/*"],},
    classifiers = ["Programming Language :: Python :: 3", "License :: OSI Approved :: MIT License",],)
