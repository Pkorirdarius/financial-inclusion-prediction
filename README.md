# Financial Inclusion Prediction

## Overview
This project utilizes machine learning to predict financial inclusion—specifically, whether an individual is likely to have a bank account. By analyzing demographic and behavioral data, the model helps identify key factors contributing to financial access.

The core prediction engine is built using a **Random Forest Classifier** and is deployed as an interactive web application using **Streamlit**.

## Features
- **Interactive UI**: A user-friendly web interface for real-time predictions.
- **Data Processing**: Automatically encodes categorical inputs (e.g., Education, Job Type) for the model.
- **Machine Learning**: Utilizes a pre-trained Random Forest model to classify eligibility.
- **Scalable**: Built with modular Python libraries including Scikit-learn and Pandas.

## Tech Stack
- **Python**: Core programming language.
- **Streamlit**: Web framework for the dashboard.
- **Scikit-learn**: Machine learning library for model inference.
- **Pandas & NumPy**: Data manipulation and numerical operations.

## Project Structure
```text
financial-inclusion-prediction/
├── app.py                # Main Streamlit application script
├── model.pkl             # Pre-trained machine learning model (Pickle format)
├── requirements.txt      # List of Python dependencies
└── README.md             # Project documentation
```

## Installation

To run this project locally, follow these steps:

### 1. Clone the repository
```bash
git clone <repository-url>
cd financial-inclusion-prediction
```

### 2. Set up a Virtual Environment (Recommended)
It is best practice to use a virtual environment to manage dependencies.

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
Install the required packages listed in `requirements.txt`:
```bash
pip install -r requirements.txt
