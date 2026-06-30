"""
E-commerce Analytics Dashboard
--------------------------------
Interactive BI dashboard built with Streamlit + Plotly.
Run locally:  streamlit run app.py
Deploy free:  Hugging Face Spaces / Streamlit Community Cloud
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta

# ──────────────────────────────────────────────────────────────────────────
# PAGE CONFIG
# ──────────────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="E-commerce Analytics Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

PRIMARY = "#2563EB"
ACCENT = "#F97316"
GREEN = "#16A34A"
RED = "#DC2626"

st.markdown(
    """
    <style>
    .stMetric { background-color: #FAFAFA; padding: 14px 16px; border-radius: 10px; border: 1px solid #EEE; }
    div[data-testid="stMetricValue"] { font-size: 1.6rem; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ──────────────────────────────────────────────────────────────────────────
# DATA GENERATION (synthetic but realistic — swap with your own CSV/DB)
# ──────────────────────────────────────────────────────────────────────────
@st.cache_data
def generate_data(seed: int = 42, n_customers: int = 2500, n_orders: int = 9000):
    rng = np.random.default_rng(seed)

    categories = ["Electronics", "Home & Kitchen", "Fashion", "Sports", "Beauty", "Books"]
    regions = ["North America", "Europe", "Latin America", "Asia Pacific"]

    start_date = datetime(2024, 1, 1)
    end_date = datetime(2025, 12, 31)
    date_range_days = (end_date - start_date).days

    customer_ids = [f"CUST-{i:05d}" for i in range(1, n_customers + 1)]
    customer_region = rng.choice(regions, size=n_customers, p=[0.35, 0.30, 0.20, 0.15])
    customer_signup = [start_date + timedelta(days=int(d)) for d in rng.integers(0, date_range_days * 0.7, n_customers)]

    customers = pd.DataFrame({
        "customer_id": customer_ids,
        "region": customer_region,
        "signup_date": customer_signup,
    })

    order_customer = rng.choice(customer_ids, size=n_orders)
    order_date_offsets = rng.integers(0, date_range_days, n_orders)
    order_dates = [start_date + timedelta(days=int(d)) for d in order_date_offsets]
    order_category = rng.choice(categories, size=n_orders, p=[0.25, 0.18, 0.22, 0.13, 0.12, 0.10])

    base_price = {"Electronics": 180, "Home & Kitchen": 65, "Fashion": 55,
                  "Sports": 70, "Beauty": 35, "Books": 18}
    order_value = [
        max(5, rng.normal(base_price[c], base_price[c] * 0.4))
        for c in order_category
    ]
    order_qty = rng.integers(1, 4, n_orders)

    orders = pd.DataFrame({
        "order_id": [f"ORD-{i:06d}" for i in range(1, n_orders + 1)],
        "customer_id": order_customer,
        "order_date": order_dates,
        "category": order_category,
        "quantity": order_qty,
        "unit_price": np.round(order_value, 2),
    })
    orders["revenue"] = (orders["quantity"] * orders["unit_price"]).round(2)
    orders = orders.merge(customers, on="customer_id", how="left")
    orders["order_date"] = pd.to_datetime(orders["order_date"])
    orders["month"] = orders["order_date"].dt.to_period("M").astype(str)

    return orders, customers


orders, customers = generate_data()

# ──────────────────────────────────────────────────────────────────────────
# SIDEBAR — FILTERS
# ──────────────────────────────────────────────────────────────────────────
st.sidebar.title("📊 Filters")

min_date, max_date = orders["order_date"].min(), orders["order_date"].max()
date_range = st.sidebar.date_input(
    "Date range",
    value=(min_date.date(), max_date.date()),
    min_value=min_date.date(),
    max_value=max_date.date(),
)

selected_regions = st.sidebar.multiselect(
    "Region", options=sorted(orders["region"].unique()), default=sorted(orders["region"].unique())
)

selected_categories = st.sidebar.multiselect(
    "Category", options=sorted(orders["category"].unique()), default=sorted(orders["category"].unique())
)

st.sidebar.markdown("---")
st.sidebar.caption("Built with Streamlit + Plotly · [View source on GitHub](https://github.com)")

# Apply filters
if len(date_range) == 2:
    start, end = date_range
    mask = (
        (orders["order_date"].dt.date >= start)
        & (orders["order_date"].dt.date <= end)
        & (orders["region"].isin(selected_regions))
        & (orders["category"].isin(selected_categories))
    )
    df = orders[mask].copy()
else:
    df = orders.copy()

# ──────────────────────────────────────────────────────────────────────────
# HEADER + KPIs
# ──────────────────────────────────────────────────────────────────────────
st.title("📊 E-commerce Analytics Dashboard")
st.caption("Synthetic demo data · Replace `generate_data()` with your own CSV/DB connection")

total_revenue = df["revenue"].sum()
total_orders = df["order_id"].nunique()
aov = total_revenue / total_orders if total_orders else 0
active_customers = df["customer_id"].nunique()

# Period-over-period comparison (vs previous equal-length period)
if len(date_range) == 2:
    period_days = (end - start).days + 1
    prev_start = start - timedelta(days=period_days)
    prev_end = start - timedelta(days=1)
    prev_mask = (
        (orders["order_date"].dt.date >= prev_start)
        & (orders["order_date"].dt.date <= prev_end)
        & (orders["region"].isin(selected_regions))
        & (orders["category"].isin(selected_categories))
    )
    prev_df = orders[prev_mask]
    prev_revenue = prev_df["revenue"].sum()
    rev_delta = ((total_revenue - prev_revenue) / prev_revenue * 100) if prev_revenue else 0
else:
    rev_delta = 0

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Revenue", f"${total_revenue:,.0f}", f"{rev_delta:+.1f}% vs prev. period")
col2.metric("Total Orders", f"{total_orders:,}")
col3.metric("Avg. Order Value", f"${aov:,.2f}")
col4.metric("Active Customers", f"{active_customers:,}")

st.markdown("---")

# ──────────────────────────────────────────────────────────────────────────
# TABS
# ──────────────────────────────────────────────────────────────────────────
tab1, tab2, tab3 = st.tabs(["📈 Revenue Trends", "👥 Cohort Retention", "🎯 RFM Segmentation"])

# ─── TAB 1: REVENUE TRENDS ──────────────────────────────────────────────────
with tab1:
    c1, c2 = st.columns([2, 1])

    with c1:
        monthly = df.groupby("month")["revenue"].sum().reset_index()
        fig = px.line(
            monthly, x="month", y="revenue", markers=True,
            title="Monthly Revenue Trend",
            color_discrete_sequence=[PRIMARY],
        )
        fig.update_layout(yaxis_title="Revenue (USD)", xaxis_title="", height=380)
        st.plotly_chart(fig, use_container_width=True)

    with c2:
        cat_rev = df.groupby("category")["revenue"].sum().sort_values(ascending=True).reset_index()
        fig2 = px.bar(
            cat_rev, x="revenue", y="category", orientation="h",
            title="Revenue by Category",
            color_discrete_sequence=[ACCENT],
        )
        fig2.update_layout(xaxis_title="Revenue (USD)", yaxis_title="", height=380)
        st.plotly_chart(fig2, use_container_width=True)

    c3, c4 = st.columns(2)
    with c3:
        region_rev = df.groupby("region")["revenue"].sum().reset_index()
        fig3 = px.pie(
            region_rev, names="region", values="revenue",
            title="Revenue Share by Region", hole=0.45,
        )
        st.plotly_chart(fig3, use_container_width=True)

    with c4:
        cat_month = df.groupby(["month", "category"])["revenue"].sum().reset_index()
        fig4 = px.area(
            cat_month, x="month", y="revenue", color="category",
            title="Revenue by Category Over Time",
        )
        fig4.update_layout(yaxis_title="Revenue (USD)", xaxis_title="")
        st.plotly_chart(fig4, use_container_width=True)

# ─── TAB 2: COHORT RETENTION ────────────────────────────────────────────────
with tab2:
    st.markdown("#### Monthly Cohort Retention Heatmap")
    st.caption("Each row is a signup cohort (by first purchase month); columns show % of customers still active N months later.")

    cohort_df = df.copy()
    cohort_df["order_period"] = cohort_df["order_date"].dt.to_period("M")
    first_purchase = cohort_df.groupby("customer_id")["order_period"].min().reset_index()
    first_purchase.columns = ["customer_id", "cohort_month"]
    #first_purchase["cohort_month"] = first_purchase["cohort_month"].astype(str)
    cohort_df = cohort_df.merge(first_purchase, on="customer_id")

    cohort_df["period_number"] = (
        (cohort_df["order_period"].dt.year - cohort_df["cohort_month"].dt.year) * 12
        + (cohort_df["order_period"].dt.month - cohort_df["cohort_month"].dt.month)
    )

    cohort_pivot = cohort_df.groupby(["cohort_month", "period_number"])["customer_id"].nunique().reset_index()
    cohort_pivot["cohort_month"] = cohort_pivot["cohort_month"].astype(str)
    cohort_counts = cohort_pivot.pivot(index="cohort_month", columns="period_number", values="customer_id")
    cohort_sizes = cohort_counts.iloc[:, 0]
    retention = cohort_counts.divide(cohort_sizes, axis=0).round(3) * 100
    retention = retention.iloc[:12, :8]  # limit for readability
    retention.index = retention.index.astype(str)
    retention.columns = retention.columns.astype(str)

    fig5 = px.imshow(
        retention,
        labels=dict(x="Months Since First Purchase", y="Cohort", color="Retention %"),
        color_continuous_scale="Blues",
        text_auto=".0f",
        aspect="auto",
    )
    fig5.update_layout(height=450, title="Retention % by Cohort Month")
    st.plotly_chart(fig5, use_container_width=True)

# ─── TAB 3: RFM SEGMENTATION ─────────────────────────────────────────────────
with tab3:
    st.markdown("#### RFM Customer Segmentation")
    st.caption("Recency, Frequency, Monetary scoring to identify customer segments for targeted campaigns.")

    snapshot_date = df["order_date"].max() + timedelta(days=1)
    rfm = df.groupby("customer_id").agg(
        recency=("order_date", lambda x: (snapshot_date - x.max()).days),
        frequency=("order_id", "nunique"),
        monetary=("revenue", "sum"),
    ).reset_index()

    rfm["R_score"] = pd.qcut(rfm["recency"], 4, labels=[4, 3, 2, 1]).astype(int)
    rfm["F_score"] = pd.qcut(rfm["frequency"].rank(method="first"), 4, labels=[1, 2, 3, 4]).astype(int)
    rfm["M_score"] = pd.qcut(rfm["monetary"], 4, labels=[1, 2, 3, 4]).astype(int)
    rfm["RFM_score"] = rfm["R_score"] + rfm["F_score"] + rfm["M_score"]

    def segment(row):
        if row["RFM_score"] >= 10:
            return "Champions"
        elif row["RFM_score"] >= 8:
            return "Loyal Customers"
        elif row["RFM_score"] >= 6:
            return "Potential Loyalists"
        elif row["RFM_score"] >= 4:
            return "At Risk"
        else:
            return "Lost"

    rfm["segment"] = rfm.apply(segment, axis=1)

    c1, c2 = st.columns([1, 2])
    with c1:
        seg_counts = rfm["segment"].value_counts().reset_index()
        seg_counts.columns = ["segment", "count"]
        fig6 = px.pie(
            seg_counts, names="segment", values="count",
            title="Customer Segments", hole=0.4,
        )
        st.plotly_chart(fig6, use_container_width=True)

    with c2:
        fig7 = px.scatter(
            rfm, x="recency", y="monetary", size="frequency", color="segment",
            title="RFM Scatter: Recency vs Monetary Value (size = Frequency)",
            hover_data=["customer_id"],
        )
        fig7.update_layout(xaxis_title="Recency (days since last order)", yaxis_title="Total Spend (USD)")
        st.plotly_chart(fig7, use_container_width=True)

    st.markdown("##### Segment Summary")
    seg_summary = rfm.groupby("segment").agg(
        customers=("customer_id", "count"),
        avg_recency=("recency", "mean"),
        avg_frequency=("frequency", "mean"),
        avg_monetary=("monetary", "mean"),
    ).round(1).sort_values("avg_monetary", ascending=False)
    st.dataframe(seg_summary, use_container_width=True)

    csv = rfm.to_csv(index=False).encode("utf-8")
    st.download_button("⬇️ Download RFM segments (CSV)", csv, "rfm_segments.csv", "text/csv")

st.markdown("---")
st.caption("Demo dashboard for portfolio purposes · Data is synthetically generated · Built by Santiago Monsalve")
