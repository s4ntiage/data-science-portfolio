# 02 — Customer Churn Prediction · Telecom

> **Classification · Feature Engineering · Explainability**

End-to-end ML pipeline to predict customer churn for a telecom company. The project emphasizes not just predictive accuracy but business interpretability — understanding *why* a customer is likely to churn, and *what threshold* maximizes profit.

---

## Highlights

- **Feature engineering** from raw customer data (tenure buckets, service count, charge trends)
- **Model comparison**: Logistic Regression, Random Forest, XGBoost, LightGBM (5-fold CV)
- **Hyperparameter tuning** with Optuna (Bayesian TPE, 40 trials)
- **SHAP** summary, bar, and waterfall plots for global and individual explanations
- **Profit curve** to find the business-optimal classification threshold

## Result

> XGBoost model with **~91% ROC-AUC**. SHAP analysis confirms that **contract type** and **tenure** are the top 2 churn drivers. Lowering the classification threshold from 0.5 to ~0.3 significantly increases estimated business profit.

---

## Structure

```
02-ml-churn/
├── notebooks/
│   └── ml_churn_prediction.ipynb   ← full pipeline
├── src/                             ← (optional) refactored .py modules
├── models/                          ← saved model artifacts
└── README.md
```

## Setup

```bash
pip install pandas numpy matplotlib seaborn scikit-learn xgboost lightgbm shap optuna
```

**Data:** Loaded automatically from the IBM GitHub repo. No manual download needed.

## Tools

![scikit-learn](https://img.shields.io/badge/-scikit--learn-F7931E?style=flat&logo=scikit-learn&logoColor=white)
![XGBoost](https://img.shields.io/badge/-XGBoost-FF6600?style=flat)
![LightGBM](https://img.shields.io/badge/-LightGBM-02569B?style=flat)
![SHAP](https://img.shields.io/badge/-SHAP-0099CC?style=flat)
![Optuna](https://img.shields.io/badge/-Optuna-6C3483?style=flat)

---

*Dataset: IBM Telco Customer Churn · License: CC0*
