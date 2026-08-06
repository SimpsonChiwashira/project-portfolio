"""
Main landing page for Churn Prediction Applications.
"""

import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Churn Prediction Hub",
    page_icon="chart",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Dark theme styling with white text
st.markdown("""
<style>
    .stApp {
        background-color: #1e1e1e;
    }
    .main {
        background-color: #1e1e1e;
    }
    h1 {
        color: #ffffff;
        font-size: 2.5rem;
        font-weight: 700;
    }
    h2 {
        color: #ffffff;
        font-size: 1.8rem;
        font-weight: 600;
    }
    h3 {
        color: #ffffff;
        font-size: 1.5rem;
        font-weight: 500;
    }
    p {
        color: #e0e0e0;
        line-height: 1.6;
    }
    .stMetric {
        background-color: #2d2d2d;
        border-radius: 5px;
        padding: 10px;
    }
    .stMetric label {
        color: #ffffff;
    }
    .stMetric div {
        color: #ffffff;
    }
</style>
""", unsafe_allow_html=True)

# Simple hero section
st.markdown("# Customer Churn Prediction Hub")
st.markdown("### Advanced Machine Learning Solutions for Customer Retention")

st.markdown("---")

# Focus on the two apps - clean and readable
st.markdown("## Available Applications")

col1, col2 = st.columns(2, gap="large")

with col1:
    with st.container(border=True):
        st.markdown("### Telco Churn Prediction")
        st.markdown("Predict telecommunications customer churn based on service usage, demographics, and account information.")
        
        st.markdown("**Features:**")
        st.markdown("- Customer demographic analysis")
        st.markdown("- Service subscription patterns")
        st.markdown("- Usage-based risk assessment")
        st.markdown("- Real-time predictions")
        
        st.markdown("**Model Performance:**")
        metric_col1, metric_col2 = st.columns(2)
        with metric_col1:
            st.metric("Accuracy", "80%")
        with metric_col2:
            st.metric("F1-Score", "61%")
        
        st.markdown("**Dataset:** Telco Customer Churn (7,043 customers)")
        
        st.markdown("")
        if st.button("Launch Telco Churn App", key="telco_btn", type="primary", use_container_width=True):
            st.switch_page("pages/telco_churn_app.py")
    
    st.markdown("")  # Add spacing

with col2:
    with st.container(border=True):
        st.markdown("### Bank Marketing Prediction")
        st.markdown("Predict likelihood of customers subscribing to term deposits based on demographics and campaign interactions.")
        
        st.markdown("**Features:**")
        st.markdown("- Demographic segmentation")
        st.markdown("- Campaign interaction analysis")
        st.markdown("- Economic factor consideration")
        st.markdown("- Target marketing optimization")
        
        st.markdown("**Model Performance:**")
        metric_col1, metric_col2 = st.columns(2)
        with metric_col1:
            st.metric("Accuracy", "86%")
        with metric_col2:
            st.metric("F1-Score", "55%")
        
        st.markdown("**Dataset:** Bank Marketing Data (45,211 customers)")
        
        st.markdown("")
        if st.button("Launch Bank Marketing App", key="bank_btn", type="primary", use_container_width=True):
            st.switch_page("pages/bank_churn_app.py")
    
    st.markdown("")  # Add spacing

st.markdown("---")

# Brief technical info
st.markdown("## Quick Technical Info")

with st.expander("Machine Learning Models Used"):
    st.markdown("- **Random Forest Classifier**: Primary model for both applications")
    st.markdown("- **Support Vector Machines (SVM)**: Evaluated during research")
    st.markdown("- **Neural Networks**: Deep learning approach using TensorFlow/Keras")
    st.markdown("- **Logistic Regression**: Baseline model for comparison")

with st.expander("Getting Started"):
    st.markdown("""
    ### 1. Install dependencies
    ```bash
    pip install -r requirements.txt
    ```
    
    ### 2. Run Streamlit apps
    ```bash
    python run_app.py
    ```
    
    ### 3. Train models (optional)
    ```bash
    python train_models.py --quick  # For quick training
    python train_models.py        # For full training with all models
    ```
    """)

st.markdown("---")
st.markdown("*Built as part of MSc Advanced Computer Science research project*")