# 01 — Airbnb Price Analysis · Mexico City

> **EDA · Geospatial · Statistical Testing**

Deep exploratory analysis of 20,000+ Airbnb listings in Mexico City using the public Inside Airbnb dataset. The goal: identify the key drivers of listing price across neighborhoods, property types, and host characteristics.

---

## Highlights

- Interactive price heatmap by colonia using **Folium**
- Outlier detection using **IQR** and **Z-score** methods
- Hypothesis testing: **Mann-Whitney U** and **Kruskal-Wallis** to validate price differences
- Correlation matrix and **Spearman feature importance** ranking
- Summary dashboard with 4 key findings visualized

## Key Finding

> Listings in Polanco and Roma Norte command a **2.3x price premium** over the city median, even after controlling for size and amenities. Statistically significant (Kruskal-Wallis, p < 0.001).

---

## Structure

```
01-eda-airbnb/
├── notebooks/
│   └── eda_airbnb_cdmx.ipynb   ← main analysis
├── data/
│   ├── listings.csv.gz          ← download from Inside Airbnb (see below)
│   └── price_heatmap_cdmx.html  ← generated interactive map
└── README.md
```

## Setup

```bash
pip install pandas numpy matplotlib seaborn folium scipy
```

**Data:** Download `listings.csv.gz` from [Inside Airbnb — Mexico City](http://insideairbnb.com/get-the-data/) and place it in `data/`. The notebook also attempts to load it directly from the URL.

## Tools

![pandas](https://img.shields.io/badge/-pandas-150458?style=flat&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/-NumPy-013243?style=flat&logo=numpy&logoColor=white)
![seaborn](https://img.shields.io/badge/-seaborn-4C72B0?style=flat)
![Folium](https://img.shields.io/badge/-Folium-77B829?style=flat)
![SciPy](https://img.shields.io/badge/-SciPy-8CAAE6?style=flat&logo=scipy&logoColor=white)

---

*Data source: [Inside Airbnb](http://insideairbnb.com) · License: CC0*
