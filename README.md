# House Prices Prediction - Advanced Regression Techniques

A machine learning project focused on predicting house prices using advanced regression techniques, feature engineering, and production-oriented pipelines.

---

## 🧭 Project Overview

This project demonstrates an end-to-end machine learning workflow, from data exploration to reusable preprocessing and model pipelines.

Using the Ames Housing dataset, multiple regression models were developed and optimized to predict residential property prices. The final selected model was XGBoost, achieving strong predictive performance.

---

## 🏆 Key Results

- **Champion Model**: XGBoost Regressor  
- **Performance**: R² = 0.9148  
- **RMSE**: $25,559  
- **Test Predictions**: 1,459 houses predicted  

---

## 📁 Project Structure

```text
house-prices-advanced-regression-techniques/
├── notebooks/                          # Jupyter notebooks (development journey)
│   ├── 01_initial_data_exploration.ipynb
│   ├── 02_model_building_and_evaluation.ipynb
│   ├── 03_pipeline_preprocessing.ipynb
│   ├── 04_pipeline_modeling.ipynb
│   └── 05_final_predictions.ipynb
├── src/                                # Source code modules
│   └── feature_engineering.py
├── models/                             # Trained model artifacts
│   ├── preprocessing_pipeline.pkl
│   ├── champion_xgboost_model.pkl
│   └── prediction_results_summary.json
├── data/                               # Dataset files
│   ├── train.csv
│   ├── test.csv
│   └── house_price_predictions.csv
└── README.md
```

---

## ⚙️ Technical Approach

### Data Preprocessing

- **ColumnTransformer Pipeline** for numerical and categorical features  
- **Feature Engineering** with domain-relevant variables  
- **Missing Value Strategy** based on feature semantics  
- **Encoding** using ordinal and one-hot approaches  

---

### Model Development

- **Algorithms Tested**:
  - Linear Regression
  - Ridge Regression
  - Lasso Regression
  - Random Forest
  - XGBoost  

- **Hyperparameter Optimization** using GridSearchCV  
- **Cross-Validation** with 5-fold CV  
- **End-to-End Pipeline** combining preprocessing and modeling  

---

### Engineered Features

- `TotalSF`: Combined square footage (1st + 2nd + Basement)  
- `TotalBath`: Total bathroom count  
- `HouseAge`: Age of house (2023 - YearBuilt)  
- `YearsSinceRemod`: Years since last remodeling  
- `WasRemodeled`: Binary indicator  

---

## 📊 Model Performance Comparison

| Model | Test R² | Test RMSE | Status |
|-------|---------|-----------|--------|
| **XGBoost** | **0.9148** | **$25,559** | **Champion** |
| Random Forest | 0.8926 | $28,703 | Strong |
| Ridge | 0.8731 | $31,198 | Baseline |
| Lasso | 0.8272 | $36,411 | Moderate |
| Linear Regression | -0.2853 | $99,290 | Poor fit |

---

## 🏗️ Production Features

- **Modular Architecture** with reusable components  
- **Pipeline Persistence** through saved artifacts  
- **Consistent Transformations** for training and inference  
- **Kaggle-Ready Output**  

---

## 🧪 Technologies Used

- Python  
- Scikit-learn  
- XGBoost  
- Pandas & NumPy  
- Matplotlib & Seaborn  
- Jupyter Notebooks  

---

## ⚙️ Reproducibility

1. Clone the repository  
2. Install dependencies  
3. Run notebooks in sequence (01 → 05)  
4. Load saved models from the `models/` directory  

---

## 💼 Potential Applications

This model can support:

- Real estate pricing decisions  
- Property valuation benchmarking  
- Investment analysis  
- Mortgage risk assessment  

---

## 👤 Contact

**Carlos Cepeda**  
[LinkedIn Profile](https://www.linkedin.com/in/ccepeda75)

Project Link:  
https://github.com/Carlos-Cepeda/house-prices-regression-portfolio




