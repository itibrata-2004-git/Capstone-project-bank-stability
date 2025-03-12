import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime
import pickle

# Load models
with open(r"C:\Users\prita\Downloads\pipeline_model.pkl", 'rb') as rf_file:
    pipeline_model = pickle.load(rf_file)


# Set page configuration
st.set_page_config(
    page_title="Bank Performance Dashboard",
    page_icon="📊",
    layout="wide"
)

# Styling
st.markdown("""
    <style>
    body {
        background-color: #1a1a2e;
        font-family: 'Segoe UI', sans-serif;
    }
    .stApp {
        background-color: #1e3a8a;
        padding: 40px;
        border-radius: 15px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    }
    .stTextInput > div > div > input {
        border: 2px solid #3B82F6;
        padding: 12px;
        border-radius: 12px;
        color: #2563EB;
        font-weight: bold;
    }
    .stButton > button {
        background-color: #3B82F6;
        color: white;
        border-radius: 10px;
        padding: 12px 20px;
        font-size: 16px;
    }
    .stSidebar {
        background-color: #1F2937;
        color: white;
    }
    .metric-container .stMetric {
        background-color: #4CAF50;
        border-radius: 8px;
        padding: 20px;
        box-shadow: 2px 4px 8px rgba(0, 0, 0, 0.2);
        color: white;
    }
    .start-button-container {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-top: 20px;
    }
    .start-button-container button {
        background-color: #10B981;
        color: white;
        font-size: 18px;
        padding: 15px 30px;
        border-radius: 12px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.15);
    }
    .start-button-container button:hover {
        background-color: #3B82F6;
    }
    </style>
""", unsafe_allow_html=True)

# Header Section
st.title("🌟 Bank Stability Performance Dashboard")
st.markdown("Welcome to the Bank Stability Performance Dashboard! Assess the financial health of banks using key performance metrics.")
st.markdown("### Click below to start the analysis:")

# Start Button to reveal the dashboard
start_button = st.button("Start Analysis", key="start_button", use_container_width=True)

if start_button:
    # Sidebar Inputs
    st.sidebar.header("🔧 Input Metrics")
    bank_name = st.sidebar.text_input("Bank Name", "Your Bank")

    capital_adequacy = st.sidebar.number_input("Capital Adequacy Ratio (%)", min_value=0.0, max_value=25.0, value=10.0, step=0.1)
    non_performing_loans = st.sidebar.number_input("Non-Performing Loans Ratio (%)", min_value=0.0, max_value=15.0, value=5.0, step=0.1)
    loan_to_deposit = st.sidebar.number_input("Loan-to-Deposit Ratio (%)", min_value=50.0, max_value=120.0, value=85.0, step=0.1)
    net_interest_margin = st.sidebar.number_input("Net Interest Margin (%)", min_value=0.0, max_value=10.0, value=3.0, step=0.1)

    # Main Dashboard Section
    st.subheader("📈 Key Metrics Analysis")

    # Key Metrics Cards
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Capital Adequacy Ratio", f"{capital_adequacy:.1f} %", "Minimum 8%")

    with col2:
        st.metric("Non-Performing Loans", f"{non_performing_loans:.1f} %", "Lower is better")

    with col3:
        st.metric("Loan-to-Deposit Ratio", f"{loan_to_deposit:.1f} %", "75-85% ideal")

    with col4:
        st.metric("Net Interest Margin", f"{net_interest_margin:.1f} %", "Higher is better")

    # Stability Score Calculation
    st.subheader("📊 Stability Score")
    stability_score = (
        (capital_adequacy / 8.0) * 25 +
        (1 - non_performing_loans / 15.0) * 25 +
        (1 - abs(loan_to_deposit - 80) / 40) * 25 +
        (net_interest_margin / 5.0) * 25
    )
    status = "Stable" if stability_score >= 75 else ("At Risk" if stability_score >= 50 else "Unstable")

    # Gauge Chart for Stability Score
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=stability_score,
        domain={'x': [0, 1], 'y': [0, 1]},
        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'color': "#2563EB"},
            'steps': [
                {'range': [0, 50], 'color': "#EF4444"},
                {'range': [50, 75], 'color': "#FBBF24"},
                {'range': [75, 100], 'color': "#10B981"}
            ]
        },
        title={'text': "Overall Stability"}
    ))

    st.plotly_chart(fig, use_container_width=True)
    st.write(f"### Current Status: {status}")

    # Recommendations Section
    st.subheader("📋 Recommendations")
    if stability_score < 50:
        st.error(f"{bank_name} is in a critical condition. Immediate intervention required.")
    elif stability_score < 75:
        st.warning(f"{bank_name} shows moderate risk. Focus on improving key metrics.")
    else:
        st.success(f"{bank_name} is performing well. Keep up the good work!")