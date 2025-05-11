# 🗽 NYC House Price Prediction App

This project predicts real estate prices for NYC properties using a stacked machine learning model that combines **XGBoost** and **Random Forest** with a **Ridge Regression** meta-learner. The app is served via **Streamlit**, includes **SHAP** model interpretability, and is trained on a curated and feature-engineered dataset.

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

## Project Structure
```
├── stacked_model.pkl             # Trained model
├── X_train_final.pkl             # Preprocessed training features
├── streamlit_app.py              # Streamlit interface
├── shap_visualization_snippet.py# SHAP code for interpretation
├── requirements.txt              # All required dependencies
└── README.md
```

## Model Performance
| Metric | Value    |
|--------|----------|
| MAE    | ~$15,804 |
| RMSE   | ~$71,319 |
| R²     | ~0.9963  |

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

## ⚠️ Disclaimer

This project is intended for educational and demonstration purposes only. The property price predictions provided by this app are generated using historical data and machine learning models trained on engineered features, and do not constitute financial, legal, or investment advice.
While every effort has been made to ensure reasonable accuracy, the model may not reflect current market conditions, zoning laws, renovation status, or other important factors. Users should consult with licensed real estate professionals before making any real-world decisions based on these predictions.
The author assumes no liability for any decisions made based on the use of this tool.