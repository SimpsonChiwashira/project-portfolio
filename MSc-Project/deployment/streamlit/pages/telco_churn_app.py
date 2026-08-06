"""
Streamlit application for Telco Customer Churn Prediction.
"""

import streamlit as st
import pandas as pd
import numpy as np
import joblib
import sys
import os

# Add the project root to the path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# Now import the modules (they may fail gracefully if dependencies aren't available)
try:
    from src.preprocessing.telco_preprocessing import TelcoDataPreprocessor
    from src.utils.visualization import setup_plotting
    PREPROCESSING_AVAILABLE = True
except ImportError as e:
    st.warning(f" preprocessing modules not available: {e}")
    PREPROCESSING_AVAILABLE = False

# Page configuration
st.set_page_config(
    page_title="Telco Churn Prediction",
    page_icon="phone",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Back to home button
if st.button("← Back to Home"):
    st.switch_page("deployment/streamlit/home.py")

st.title("Telco Customer Churn Prediction")
st.markdown("Predict whether a telecommunications customer will churn based on their service usage and demographics.")

# Model selection
st.sidebar.header("Model Selection")
model_options = {
    'random_forest': {
        'name': 'Random Forest',
        'accuracy': '80%',
        'f1_score': '61%',
        'description': 'Best overall performance, higher recall for churn detection'
    },
    'svm': {
        'name': 'Support Vector Machine (SVM)',
        'accuracy': '76%',
        'f1_score': '48%',
        'description': 'Good for complex decision boundaries, can be slow'
    },
    'logistic_regression': {
        'name': 'Logistic Regression',
        'accuracy': '79%',
        'f1_score': '61%',
        'description': 'Good balance, faster predictions, interpretable'
    },
    'neural_network': {
        'name': 'Neural Network',
        'accuracy': '78%',
        'f1_score': '59%',
        'description': 'Deep learning approach, complex patterns'
    }
}

# Check which models are available
available_models = []
for model_key, model_name in model_options.items():
    model_path = os.path.join(project_root, f'models/telco_{model_key}_model.pkl')
    if os.path.exists(model_path):
        available_models.append(model_key)

# Fallback to old naming if new naming doesn't exist
if not available_models:
    for model_key, model_name in model_options.items():
        if model_key == 'random_forest':
            old_path = os.path.join(project_root, 'models/telco_rf_model.pkl')
            if os.path.exists(old_path):
                available_models.append(model_key)

if available_models:
    selected_model = st.sidebar.selectbox(
        "Choose Model",
        options=available_models,
        format_func=lambda x: model_options[x]['name'],
        index=0 if 'random_forest' in available_models else 0
    )
else:
    selected_model = 'random_forest'
    st.sidebar.warning("No trained models found. Using demo mode.")

# Load the model and preprocessor
@st.cache_resource
def load_model_and_preprocessor(model_type='random_forest'):
    """Load the trained model and preprocessor."""
    try:
        # Try new naming convention first
        model_path = os.path.join(project_root, f'models/telco_{model_type}_model.pkl')
        
        # Fallback to old naming convention for random forest
        if not os.path.exists(model_path) and model_type == 'random_forest':
            model_path = os.path.join(project_root, 'models/telco_rf_model.pkl')
        
        # Try scaler (updated preprocessing approach)
        scaler_path = os.path.join(project_root, 'models/telco_scaler.pkl')
        
        # Fallback to preprocessor (old approach)
        if not os.path.exists(scaler_path):
            scaler_path = os.path.join(project_root, 'models/telco_preprocessor.pkl')
        
        if os.path.exists(model_path) and os.path.exists(scaler_path):
            model = joblib.load(model_path)
            preprocessor = joblib.load(scaler_path)
            return model, preprocessor, "Trained Model"
        else:
            return None, None, "Demo Mode"
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None, None, "Error"

model, preprocessor, mode = load_model_and_preprocessor(selected_model)

if mode == "Demo Mode":
    st.warning("No trained model found. Running in demo mode with simulated predictions.")
    st.info("To use the full prediction system, train models using: python train_models.py")
elif mode == "Trained Model":
    st.success(f"{model_options[selected_model]['name']} model loaded successfully!")
    
    # Dynamic model information based on selection
    model_info = model_options.get(selected_model, {})
    st.sidebar.info(f"""
**Model Performance:**
- **Algorithm:** {model_info.get('name', 'Unknown')}
- **Accuracy:** {model_info.get('accuracy', 'N/A')}
- **F1-Score:** {model_info.get('f1_score', 'N/A')}
- **Description:** {model_info.get('description', 'N/A')}
""")

# Main input form
st.header("Customer Information")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Demographics")
    gender = st.selectbox("Gender", ["Male", "Female"])
    senior_citizen = st.selectbox("Senior Citizen", ["No", "Yes"])
    partner = st.selectbox("Partner", ["No", "Yes"])
    dependents = st.selectbox("Dependents", ["No", "Yes"])

with col2:
    st.subheader("Services")
    phone_service = st.selectbox("Phone Service", ["No", "Yes"])
    multiple_lines = st.selectbox("Multiple Lines", ["No", "Yes", "No phone service"])
    internet_service = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
    online_security = st.selectbox("Online Security", ["No", "Yes", "No internet service"])

with col3:
    st.subheader("Contract & Billing")
    contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
    paperless_billing = st.selectbox("Paperless Billing", ["No", "Yes"])
    payment_method = st.selectbox("Payment Method", 
        ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"])
    tenure = st.slider("Tenure (months)", 0, 72, 12)
    monthly_charges = st.number_input("Monthly Charges", 0.0, 200.0, 50.0)
    total_charges = st.number_input("Total Charges", 0.0, 10000.0, 600.0)

# Make prediction
if st.button("Predict Churn Risk", type="primary"):
    if mode == "Demo Mode":
        # Simulate prediction in demo mode
        churn_probability = np.random.uniform(0.3, 0.7)
        churn_risk = "High" if churn_probability > 0.5 else "Low"
    else:
        # Real prediction using trained model
        try:
            # Create input DataFrame
            input_data = pd.DataFrame([{
                'gender': gender,
                'SeniorCitizen': 1 if senior_citizen == "Yes" else 0,
                'Partner': partner,
                'Dependents': dependents,
                'tenure': tenure,
                'PhoneService': phone_service,
                'MultipleLines': multiple_lines,
                'InternetService': internet_service,
                'OnlineSecurity': online_security,
                'Contract': contract,
                'PaperlessBilling': paperless_billing,
                'PaymentMethod': payment_method,
                'MonthlyCharges': monthly_charges,
                'TotalCharges': total_charges
            }])
            
            # Preprocess and predict
            if preprocessor:
                input_processed = preprocessor.transform(input_data)
                churn_probability = model.predict_proba(input_processed)[0][1]
                churn_risk = "High" if churn_probability > 0.5 else "Low"
            else:
                churn_probability = 0.5
                churn_risk = "Medium"
        except Exception as e:
            st.error(f"Prediction error: {e}")
            churn_probability = 0.5
            churn_risk = "Medium"
    
    # Display results
    st.markdown("---")
    st.header("Prediction Results")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric("Churn Probability", f"{churn_probability:.2%}")
    
    with col2:
        risk_color = "🔴" if churn_risk == "High" else "🟢" if churn_risk == "Low" else "🟡"
        st.metric("Churn Risk", f"{risk_color} {churn_risk}")
    
    # Additional insights
    st.markdown("---")
    st.subheader("Insights")
    
    if churn_risk == "High":
        st.warning("""
        **High Churn Risk Detected**
        
        This customer shows signs of potential churn. Consider:
        - Offering promotional deals or discounts
        - Improving customer service interaction
        - Addressing service quality issues
        - Providing loyalty incentives
        """)
    elif churn_risk == "Low":
        st.success("""
        **Low Churn Risk**
        
        This customer appears satisfied with the service. Maintain:
        - Current service quality
        - Regular check-ins
        - Loyalty programs
        - Proactive support
        """)
    else:
        st.info("""
        **Medium Churn Risk**
        
        This customer shows moderate churn indicators. Monitor:
        - Service usage patterns
        - Payment history
        - Support interactions
        - Competitor offers
        """)

# Footer
st.markdown("---")
st.markdown("*Built with Streamlit and Machine Learning*")