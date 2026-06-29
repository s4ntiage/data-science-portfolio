# Data Science Portfolio

> Freelance Data Scientist · EDA · Machine Learning · NLP · Deep Learning · Data Visualization · SQL

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)](https://python.org)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebooks-F37626?style=flat&logo=jupyter&logoColor=white)](https://jupyter.org)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-F7931E?style=flat&logo=scikit-learn&logoColor=white)](https://scikit-learn.org)
[![PyTorch](https://img.shields.io/badge/PyTorch-Deep%20Learning-EE4C2C?style=flat&logo=pytorch&logoColor=white)](https://pytorch.org)
[![Upwork](https://img.shields.io/badge/Available%20on-Upwork-6FDA44?style=flat)](https://upwork.com)

---

## About

I'm a data scientist specializing in turning raw data into actionable insights and production-ready models. I work across the full data pipeline — from exploratory analysis and feature engineering to model deployment and interactive dashboards.

I'm available for freelance projects on Upwork and beyond. If you have a data problem to solve, let's talk.

📧 **smonsalvemsantiago@email.com** · 💼 **[Upwork Profile](https://www.upwork.com/freelancers/~015055a50708a2cd76?mp_source=share)** · 🌐 **[LinkedIn](https://www.linkedin.com/in/monsalvesantiago/)**

---

## Projects

| # | Project | Area | Tools | Live Demo |
|---|---------|------|-------|-----------|
| 01 | [Airbnb Price Analysis — Mexico City](#01---airbnb-price-analysis) | EDA | pandas, seaborn, folium, scipy | — |
| 02 | [Customer Churn Prediction — Telecom](#02---customer-churn-prediction) | Machine Learning | xgboost, shap, optuna, sklearn | — |
| 03 | [E-commerce Analytics Dashboard](#03---e-commerce-analytics-dashboard) | Visualization | plotly, streamlit, pandas | [Live App ↗](https://huggingface.co) |
| 04 | [Product Review Analyzer — Amazon](#04---product-review-analyzer) | NLP | transformers, BERTopic, torch | — |
| 05 | [Sales Analytics with Advanced SQL](#05---sales-analytics-with-sql) | SQL | postgresql, dbt, python | — |
| 06 | [Medical Image Classifier — X-Ray](#06---medical-image-classifier) | Deep Learning | pytorch, torchvision, grad-cam, wandb | — |

---

## Skills at a Glance

### Languages & Core
![Python](https://img.shields.io/badge/-Python-3776AB?style=flat&logo=python&logoColor=white)
![SQL](https://img.shields.io/badge/-SQL-4479A1?style=flat&logo=postgresql&logoColor=white)
![R](https://img.shields.io/badge/-R-276DC3?style=flat&logo=r&logoColor=white)

### Data & ML
![pandas](https://img.shields.io/badge/-pandas-150458?style=flat&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/-NumPy-013243?style=flat&logo=numpy&logoColor=white)
![scikit-learn](https://img.shields.io/badge/-scikit--learn-F7931E?style=flat&logo=scikit-learn&logoColor=white)
![XGBoost](https://img.shields.io/badge/-XGBoost-FF6600?style=flat)
![SHAP](https://img.shields.io/badge/-SHAP-0099CC?style=flat)

### Deep Learning & NLP
![PyTorch](https://img.shields.io/badge/-PyTorch-EE4C2C?style=flat&logo=pytorch&logoColor=white)
![HuggingFace](https://img.shields.io/badge/-HuggingFace-FFD21E?style=flat&logo=huggingface&logoColor=black)
![BERT](https://img.shields.io/badge/-BERT/Transformers-FF6F00?style=flat)

### Visualization & Deployment
![Plotly](https://img.shields.io/badge/-Plotly-3F4F75?style=flat&logo=plotly&logoColor=white)
![Streamlit](https://img.shields.io/badge/-Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)
![Tableau](https://img.shields.io/badge/-Tableau-E97627?style=flat&logo=tableau&logoColor=white)

---

## Project Details

### 01 — Airbnb Price Analysis

**`EDA · Geospatial · Statistical Testing`**

Deep exploratory analysis of 20,000+ Airbnb listings in Mexico City using the public Inside Airbnb dataset. The goal was to identify the key drivers of listing price across neighborhoods, property types, and host characteristics.

**Highlights:**
- Interactive heatmap of price distribution by colonia using Folium
- Outlier detection and analysis using IQR and Z-score methods
- Hypothesis testing (Mann-Whitney U, Kruskal-Wallis) to validate price differences across zones
- Correlation matrix and feature importance ranking for pricing factors

**Key finding:** Listings in Polanco and Roma Norte command a 2.3x price premium over the city median, even after controlling for size and amenities.

📁 [`01-eda-airbnb/`](./01-eda-airbnb/)

---

### 02 — Customer Churn Prediction

**`Classification · Feature Engineering · Explainability`**

End-to-end ML pipeline to predict customer churn for a telecom company. The project emphasizes not just predictive accuracy but business interpretability — understanding *why* a customer is likely to churn.

**Highlights:**
- Feature engineering from raw usage logs (recency, frequency, trend features)
- Model comparison: Logistic Regression, Random Forest, XGBoost, LightGBM
- Hyperparameter tuning with Optuna (Bayesian optimization)
- SHAP waterfall plots for individual prediction explanations
- Business-oriented evaluation: profit curves and threshold optimization

**Result:** XGBoost model with 91% AUC; SHAP analysis revealed that contract type and tenure are the top 2 churn drivers.

📁 [`02-ml-churn/`](./02-ml-churn/)

---

### 03 — E-commerce Analytics Dashboard

**`Streamlit · Plotly · Cohort Analysis`**

Interactive business intelligence dashboard built with Streamlit and Plotly, simulating a real e-commerce analytics suite. Fully deployed and accessible without running any code.

**Highlights:**
- KPI cards: revenue, orders, AOV, and customer retention rate
- Cohort retention heatmap (monthly)
- Revenue breakdown by product category and region
- RFM (Recency, Frequency, Monetary) customer segmentation
- Date range filters and downloadable reports

**Live app:** [View on Hugging Face Spaces ↗](https://huggingface.co)

📁 [`03-dashboard-ecommerce/`](./03-dashboard-ecommerce/)

---

### 04 — Product Review Analyzer

**`NLP · Sentiment Analysis · Topic Modeling`**

NLP pipeline to extract insights from Amazon product reviews at scale. Compares classical sentiment analysis with fine-tuned BERT, and uses BERTopic for unsupervised topic discovery.

**Highlights:**
- VADER vs fine-tuned DistilBERT sentiment comparison
- BERTopic topic modeling with interactive visualization
- Named entity recognition to extract product features mentioned in reviews
- Sentiment trend over time per product category
- Model card with evaluation metrics and limitations

**Key finding:** BERT outperforms VADER by 14 points F1 on sarcastic and mixed-sentiment reviews.

📁 [`04-nlp-reviews/`](./04-nlp-reviews/)

---

### 05 — Sales Analytics with SQL

**`PostgreSQL · Window Functions · dbt · CTEs`**

A complete analytics project built in SQL from scratch — schema design, data loading, and progressively complex queries from basic aggregations to advanced window functions, cohort analysis, and dbt models.

**Highlights:**
- Entity-Relationship Diagram (ERD) of the schema
- 30+ queries organized by complexity level (basic → advanced)
- Cohort retention analysis using window functions
- Revenue attribution and funnel analysis with CTEs
- dbt models for a clean analytics layer
- Python notebook to visualize query results

📁 [`05-sql-ventas/`](./05-sql-ventas/)

---

### 06 — Medical Image Classifier

**`CNN · Transfer Learning · Grad-CAM · Experiment Tracking`**

Deep learning classifier for chest X-ray images (pneumonia detection) using ResNet50 with transfer learning. The project goes beyond accuracy — it includes interpretability via Grad-CAM activation maps and full experiment tracking with Weights & Biases.

**Highlights:**
- ResNet50 fine-tuned on NIH Chest X-ray dataset
- Data augmentation pipeline for medical imaging
- Grad-CAM heatmaps showing which regions the model uses for decisions
- Full experiment tracking with W&B (learning curves, hyperparameters, artifacts)
- Confusion matrix and per-class ROC curves

**Result:** 93.2% accuracy with AUC 0.97; Grad-CAM confirms the model focuses on clinically relevant lung regions.

📁 [`06-dl-imagenes/`](./06-dl-imagenes/)

---

## Repository Structure

```
data-science-portfolio/
│
├── 01-eda-airbnb/
│   ├── notebooks/
│   ├── data/
│   └── README.md
│
├── 02-ml-churn/
│   ├── notebooks/
│   ├── src/
│   ├── models/
│   └── README.md
│
├── 03-dashboard-ecommerce/
│   ├── app/
│   ├── data/
│   └── README.md
│
├── 04-nlp-reviews/
│   ├── notebooks/
│   ├── src/
│   └── README.md
│
├── 05-sql-ventas/
│   ├── queries/
│   ├── schema/
│   ├── notebooks/
│   └── README.md
│
├── 06-dl-imagenes/
│   ├── notebooks/
│   ├── src/
│   ├── experiments/
│   └── README.md
│
└── README.md   ← you are here
```

---

## Let's Work Together

I'm available for freelance engagements, short-term projects, and long-term collaborations. Typical projects I take on:

- Exploratory data analysis and reporting
- Machine learning model development and deployment
- Data pipeline design and automation
- Dashboard and visualization development
- NLP solutions (classification, extraction, generation)
- Deep learning for vision or text

📧 **smonsalvemsantiago@email.com** · 💼 **[Upwork Profile](https://www.upwork.com/freelancers/~015055a50708a2cd76?mp_source=share)** · 🌐 **[LinkedIn](https://www.linkedin.com/in/monsalvesantiago/)**

---

<p align="center">
  <sub>Built with Python, curiosity, and a lot of coffee.</sub>
</p>
