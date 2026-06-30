# 03 — E-commerce Analytics Dashboard

> **Streamlit · Plotly · Cohort Analysis**

Interactive business intelligence dashboard simulating a real e-commerce analytics suite. Fully deployed and accessible without running any code — the link below opens a live app.

🔗 **Live demo:** [your-deployed-link-here](https://huggingface.co) *(update after deploying — see below)*

---

## Highlights

- **KPI cards**: revenue, orders, AOV, active customers, with period-over-period comparison
- **Cohort retention heatmap**: monthly retention by signup cohort
- **Revenue breakdown**: by category, region, and time, with interactive Plotly charts
- **RFM segmentation**: Recency-Frequency-Monetary customer segmentation with scatter plot and downloadable CSV
- **Sidebar filters**: date range, region, and category — all charts update live

---

## Structure

```
03-dashboard-ecommerce/
├── app/
│   ├── app.py             ← main Streamlit app
│   └── requirements.txt
├── data/                   ← (optional) place your own CSV here
└── README.md
```

## Run locally

```bash
cd app
pip install -r requirements.txt
streamlit run app.py
```

The app opens at `http://localhost:8501`. It ships with realistic **synthetic data** generated on the fly (2 years, 2,500 customers, 9,000 orders) — no setup needed to see it working. To use real data, replace the `generate_data()` function with a `pd.read_csv()` or database call.

## Deploy for free (so you have a live link for Upwork/clients)

**Option A — Streamlit Community Cloud** (easiest)
1. Push this folder to a public GitHub repo
2. Go to [share.streamlit.io](https://share.streamlit.io), connect your repo
3. Point it to `app/app.py` → deploy

**Option B — Hugging Face Spaces**
1. Create a new Space → SDK: Streamlit
2. Upload `app.py` and `requirements.txt`
3. It builds and deploys automatically

Once deployed, update the live demo link at the top of this README and in the main portfolio README.

## Tools

![Streamlit](https://img.shields.io/badge/-Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)
![Plotly](https://img.shields.io/badge/-Plotly-3F4F75?style=flat&logo=plotly&logoColor=white)
![pandas](https://img.shields.io/badge/-pandas-150458?style=flat&logo=pandas&logoColor=white)

---

*Demo dashboard for portfolio purposes · Data is synthetically generated*
