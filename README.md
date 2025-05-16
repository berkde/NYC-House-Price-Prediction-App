# 🗽 NYC House Price Prediction App

This project predicts housing prices in New York City using a stacked machine learning model that combines **XGBoost** and **Random Forest** with a **Ridge Regression** meta-learner based on publicly available data.
It demonstrates an end-to-end machine learning pipeline, from raw data preprocessing to model deployment using Streamlit.

---

### Problem Statement

Accurately predicting real estate prices is critical for buyers, sellers, and investors. This app attempts to build a regression model that estimates housing prices based on features like square footage, number of rooms, location, and amenities.

---

### Approach

1. **Data Cleaning**:

   * Removed nulls, duplicates, and outliers
   * Standardized formats for price, size, etc.

2. **Feature Engineering**:

   * Extracted `price_per_sqft`, encoded categorical variables
   * Removed multicollinear features

3. **Model Training**:

   * Algorithm: `RandomForestRegressor`
   * Evaluation: MAE, RMSE, R²

4. **Deployment**:

   * Built an interactive web app using [Streamlit](https://streamlit.io/)
   * Supports user-uploaded custom listings for price prediction

---

### Repo Structure

```bash
├── app/                 # Streamlit UI code
├── data/                # Input CSV data
├── model/               # Trained model artifacts
├── notebooks/           # EDA and training notebooks
├── requirements.txt     # Dependencies
├── README.md
└── streamlit_app.py     # Entry point
```

---

###  Dataset

* **Source**: [Kaggle / NYC Housing](https://www.kaggle.com/datasets/nelgiriyewithana/new-york-housing-market)
* **Features** include:

  * `price`, `sqft`, `bedrooms`, `bathrooms`, `location`, `type`, etc.
* **Rows**: \~4,500

---

## Features
- Ensemble model with XGBoost + Random Forest
- Log-transformed price predictions
- SHAP feature importance visualization
- Auto-engineered features like:
  - `PRICE_PER_BATH`
  - `SQFT_PER_BED`
  - `DIST_TO_MIDTOWN_KM`
- Interactive Streamlit UI
- Easily extensible and deployable

---

## Project Structure
```
├── stacked_model.pkl             # Trained model
├── X_train_final.pkl             # Preprocessed training features
├── streamlit_app.py              # Streamlit interface
├── shap_visualization_snippet.py# SHAP code for interpretation
├── requirements.txt              # All required dependencies
└── README.md
```

---

## Model Performance
| Metric | Value    |
|--------|----------|
| MAE    | ~$15,804 |
| RMSE   | ~$71,319 |
| R²     | ~0.9963  |

---

## Setup Instructions

```bash
git clone https://github.com/your-username/nyc-price-predictor.git
cd nyc-price-predictor
pip install -r requirements.txt
streamlit run streamlit_app.py
```

## Requirements
See `requirements.txt` for dependencies.

## Visualization

The app includes a SHAP-based feature importance chart that shows what drives predictions.

---

## Limitations & Future Work

* **Not scalable** for real-time inference or production loads
* Currently limited to static model inference
* Model retraining is manual

### **Next Steps**:

* Integrate with PostgreSQL for data persistence
* Build REST API using FastAPI or Flask
* Add model monitoring with MLflow
* Deploy using Docker + GCP

---

## ✅ Upcoming improvements are tracked [here](https://github.com/berkde/NYC-House-Price-Prediction-App/issues)


---

## Author

### Berk Delibalta – [LinkedIn](https://www.linkedin.com/in/berkdelibalta/) | [GitHub](https://github.com/berkde)

---

## ⚠️ Disclaimer

This project is intended for educational and demonstration purposes only. The property price predictions provided by this app are generated using historical data and machine learning models trained on engineered features, and do not constitute financial, legal, or investment advice.
While every effort has been made to ensure reasonable accuracy, the model may not reflect current market conditions, zoning laws, renovation status, or other important factors. Users should consult with licensed real estate professionals before making any real-world decisions based on these predictions.
The author assumes no liability for any decisions made based on the use of this tool.

---

> This project was originally built as a personal prototype to explore regression modeling and Streamlit deployment. It is now being incrementally upgraded toward a more production-like architecture with MLOps practices. Feedback and contributions welcome.
