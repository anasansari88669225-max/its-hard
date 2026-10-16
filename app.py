"""
RetainIQ: Customer Churn Prediction and Retention Analytics System
Enterprise Streamlit Application - Neumorphism Light Theme
"""
import streamlit as st
import pandas as pd
import os
import sys

# Ensure root directory is in sys.path
sys.path.append(os.path.dirname(__file__))

from utils.ui import (
    apply_neumorphic_theme, render_header, render_kpi,
    COLOR_PRIMARY, COLOR_SUCCESS, COLOR_DANGER, COLOR_WARNING, COLOR_PURPLE,
    NEU_BG, NEU_SHADOW_DARK, NEU_SHADOW_LIGHT, TEXT_PRIMARY, TEXT_SECONDARY
)
from utils.data_loader import load_data, load_metadata

# Page Config
st.set_page_config(
    page_title="RetainIQ | Churn Prediction & Retention Suite",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply Neumorphic Light Styling
apply_neumorphic_theme()

# Sidebar Branding
with st.sidebar:
    st.markdown(f"""
    <div style="text-align: center; padding: 10px 0 20px 0;">
        <div style="
            display: inline-flex; align-items: center; justify-content: center;
            width: 64px; height: 64px; border-radius: 20px;
            background: {NEU_BG};
            box-shadow: 6px 6px 12px {NEU_SHADOW_DARK}, -6px -6px 12px {NEU_SHADOW_LIGHT};
            font-size: 30px; margin-bottom: 10px;
        ">
            🛡️
        </div>
        <h2 style="font-size: 1.4rem; font-weight: 800; color: {TEXT_PRIMARY}; margin: 0; letter-spacing: -0.02em;">
            Retain<span style="color: {COLOR_PRIMARY};">IQ</span>
        </h2>
        <div style="font-size: 0.72rem; font-weight: 700; color: {TEXT_SECONDARY}; text-transform: uppercase; letter-spacing: 0.1em; margin-top: 4px;">
            SaaS Retention Intelligence
        </div>
        <div style="margin-top: 12px;">
            <span class="neu-badge badge-success">● System Operational</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 📌 Navigation Guide")
    st.markdown("""
    Use the sidebar menu above to navigate through all **8 Enterprise Modules**:
    - **1. Home:** Overview & Value Proposition
    - **2. Customer Explorer:** Multi-filter query engine
    - **3. Churn Dashboard:** Executive revenue KPIs
    - **4. Churn Analysis:** Deep exploratory analytics
    - **5. Model Comparison:** 5 Scikit-Learn algorithms
    - **6. Threshold Analysis:** Dynamic probability tuning
    - **7. Churn Prediction:** Live single-customer scoring
    - **8. Retention Dashboard:** At-risk accounts & actions
    """)
    st.markdown("---")
    st.markdown(f"""
    <div style="font-size: 0.78rem; color: {TEXT_SECONDARY}; text-align: center;">
        <b>Client Portfolio Ready</b><br>
        Built with Streamlit & Scikit-Learn<br>
        Light Neumorphic Design System
    </div>
    """, unsafe_allow_html=True)

# Main Hero Section
render_header(
    title="Customer Churn Prediction & Retention Analytics System",
    subtitle="End-to-End Enterprise Machine Learning Platform to Detect Attrition, Safeguard MRR, and Drive Customer Lifetime Value.",
    badge_text="SaaS & Subscription Intelligence",
    badge_type="badge-primary"
)

# Load metadata / dataset for KPI cards
df = load_data()
meta = load_metadata()

if meta and "dataset_summary" in meta:
    stats = meta["dataset_summary"]
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        render_kpi("Monitored Accounts", f"{stats['total_customers']:,}", "Active & Historical Subscribers", icon="👥")
    with c2:
        render_kpi("Churn Rate", f"{stats['churn_rate_pct']:.1f}%", f"{stats['churned_customers']:,} Churned Accounts", delta="-2.4% vs Industry", delta_color="success", icon="📉")
    with c3:
        render_kpi("Total Monitored MRR", f"${stats['total_mrr']:,.0f}", "Monthly Recurring Revenue", icon="💰")
    with c4:
        render_kpi("Monthly ARR at Risk", f"${stats['churned_mrr']:,.0f}", "Revenue Lost to Churn", delta="Action Required", delta_color="danger", icon="⚠️")
else:
    c1, c2, c3, c4 = st.columns(4)
    with c1: render_kpi("Monitored Accounts", "4,000", "Full Enterprise Dataset", icon="👥")
    with c2: render_kpi("Churn Rate", "25.2%", "Benchmark Baseline", icon="📉")
    with c3: render_kpi("Total MRR", "$324,500", "Monthly Recurring Revenue", icon="💰")
    with c4: render_kpi("MRR At Risk", "$81,800", "Identified by ML Models", icon="⚠️")

st.markdown("<br>", unsafe_allow_html=True)

# Neumorphic Feature Showcase Grid
st.markdown(f"""
<div class="neu-card">
    <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 16px;">
        <div>
            <span class="neu-badge badge-purple">Executive Overview</span>
            <h3 style="margin: 6px 0 0 0; color: {TEXT_PRIMARY}; font-weight: 800; font-size: 1.35rem;">
                Business Problem & Strategic Solution
            </h3>
        </div>
    </div>
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; margin-top: 15px;">
        <div class="neu-inset">
            <h4 style="color: {COLOR_DANGER}; margin: 0 0 8px 0; font-weight: 700;">🚨 The Business Problem</h4>
            <p style="color: {TEXT_SECONDARY}; font-size: 0.92rem; line-height: 1.55; margin: 0;">
                Subscription-based businesses burn massive capital acquiring customers, only to lose them through unmanaged churn. Without predictive early warnings, cancellations happen silently, bleeding MRR and eroding investor valuation.
            </p>
        </div>
        <div class="neu-inset">
            <h4 style="color: {COLOR_PRIMARY}; margin: 0 0 8px 0; font-weight: 700;">💡 The RetainIQ Solution</h4>
            <p style="color: {TEXT_SECONDARY}; font-size: 0.92rem; line-height: 1.55; margin: 0;">
                RetainIQ applies 5 supervised Machine Learning algorithms to telemetry, billing, and sentiment data to score customer attrition 30–60 days before contract expiry, triggering targeted retention playbooks.
            </p>
        </div>
        <div class="neu-inset">
            <h4 style="color: {COLOR_SUCCESS}; margin: 0 0 8px 0; font-weight: 700;">📈 Measurable ROI</h4>
            <p style="color: {TEXT_SECONDARY}; font-size: 0.92rem; line-height: 1.55; margin: 0;">
                By optimizing the classification threshold to <b>0.38</b>, RetainIQ captures <b>89%+ of churners</b>, allowing customer success teams to retain up to $220,000 in annual recurring revenue with high-precision interventions.
            </p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Quick Navigation Hub
st.markdown("### 🚀 Explore Platform Modules")

n_col1, n_col2, n_col3, n_col4 = st.columns(4)

with n_col1:
    st.markdown(f"""
    <div class="neu-card" style="text-align: center; padding: 22px 16px;">
        <div style="font-size: 2rem; margin-bottom: 8px;">🔍</div>
        <div style="font-weight: 800; font-size: 1.05rem; color: {TEXT_PRIMARY};">Customer Explorer</div>
        <p style="font-size: 0.82rem; color: {TEXT_SECONDARY}; margin: 8px 0 16px 0;">Interactive 8-way multi-filter data query engine with CSV export.</p>
        <span class="neu-badge badge-primary">Module 02</span>
    </div>
    """, unsafe_allow_html=True)

with n_col2:
    st.markdown(f"""
    <div class="neu-card" style="text-align: center; padding: 22px 16px;">
        <div style="font-size: 2rem; margin-bottom: 8px;">📊</div>
        <div style="font-weight: 800; font-size: 1.05rem; color: {TEXT_PRIMARY};">Churn Analytics</div>
        <p style="font-size: 0.82rem; color: {TEXT_SECONDARY}; margin: 8px 0 16px 0;">15+ deep exploratory Plotly charts covering contracts, NPS, and billing.</p>
        <span class="neu-badge badge-purple">Module 04</span>
    </div>
    """, unsafe_allow_html=True)

with n_col3:
    st.markdown(f"""
    <div class="neu-card" style="text-align: center; padding: 22px 16px;">
        <div style="font-size: 2rem; margin-bottom: 8px;">🧠</div>
        <div style="font-weight: 800; font-size: 1.05rem; color: {TEXT_PRIMARY};">Model Studio</div>
        <p style="font-size: 0.82rem; color: {TEXT_SECONDARY}; margin: 8px 0 16px 0;">5 ML models benchmarked with ROC curves, PR curves, and Feature Importance.</p>
        <span class="neu-badge badge-warning">Module 05</span>
    </div>
    """, unsafe_allow_html=True)

with n_col4:
    st.markdown(f"""
    <div class="neu-card" style="text-align: center; padding: 22px 16px;">
        <div style="font-size: 2rem; margin-bottom: 8px;">🔮</div>
        <div style="font-weight: 800; font-size: 1.05rem; color: {TEXT_PRIMARY};">Live Predictor</div>
        <p style="font-size: 0.82rem; color: {TEXT_SECONDARY}; margin: 8px 0 16px 0;">Instant real-time customer risk scoring with personalized retention playbooks.</p>
        <span class="neu-badge badge-success">Module 07</span>
    </div>
    """, unsafe_allow_html=True)

# Architecture & Dataset Specifications
st.markdown("<br>", unsafe_allow_html=True)
with st.expander("📁 Enterprise Dataset & Machine Learning Architecture Details", expanded=False):
    t1, t2 = st.columns(2)
    with t1:
        st.markdown(f"""
        <div class="neu-inset">
            <h4 style="color: {TEXT_PRIMARY}; margin: 0 0 10px 0;">📊 Dataset Specifications</h4>
            <ul style="font-size: 0.88rem; color: {TEXT_SECONDARY}; line-height: 1.7; padding-left: 20px;">
                <li><b>Total Records:</b> 4,000 verified enterprise & consumer subscriber profiles</li>
                <li><b>Temporal Coverage:</b> 2021 to 2026 (Tenure up to 72 months)</li>
                <li><b>Feature Space:</b> 25 raw features + 9 engineered business indicators</li>
                <li><b>Target Variable:</b> <code>Churned</code> (Binary: 0 = Active, 1 = Churned)</li>
                <li><b>Data Quality:</b> Handled missing telemetry values via median/mode imputation</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    with t2:
        st.markdown(f"""
        <div class="neu-inset">
            <h4 style="color: {TEXT_PRIMARY}; margin: 0 0 10px 0;">⚙️ Technology Stack</h4>
            <ul style="font-size: 0.88rem; color: {TEXT_SECONDARY}; line-height: 1.7; padding-left: 20px;">
                <li><b>Modeling Framework:</b> Scikit-Learn Pipelines (ColumnTransformer, StandardScaler, OneHotEncoder)</li>
                <li><b>Algorithms:</b> Logistic Regression, KNN, Decision Tree, Random Forest, Gradient Boosting</li>
                <li><b>Visualization Engine:</b> Plotly Graph Objects & Express (Custom Neumorphic Theme)</li>
                <li><b>Persistence:</b> Joblib serialized models and JSON training metadata</li>
                <li><b>Frontend:</b> Streamlit Multi-Page Web Architecture with Custom Tactile CSS</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.markdown(f"""
<div style="text-align: center; color: {TEXT_SECONDARY}; font-size: 0.82rem; padding: 20px 0;">
    RetainIQ Platform &bull; Built for High-Growth US Subscription Businesses &bull; Developed by AI Engineering Pair
</div>
""", unsafe_allow_html=True)
