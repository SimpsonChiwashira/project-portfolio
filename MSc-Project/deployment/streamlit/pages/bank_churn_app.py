"""
Streamlit application for Bank Marketing Churn Prediction.
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
    from src.preprocessing.bank_preprocessing import BankDataPreprocessor
    from src.utils.visualization import setup_plotting
    PREPROCESSING_AVAILABLE = True
except ImportError as e:
    st.warning(f" preprocessing modules not available: {e}")
    PREPROCESSING_AVAILABLE = False

# Page configuration
st.set_page_config(
    page_title="Bank Marketing Prediction",
    page_icon="bank",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Back to home button
if st.button("← Back to Home"):
    st.switch_page("deployment/streamlit/home.py")

st.title("Bank Marketing Prediction")
st.markdown("Predict likelihood of customers subscribing to term deposits based on demographics and campaign interactions.")

# Model selection
st.sidebar.header("Model Selection")
model_options = {
    'random_forest': {
        'name': 'Random Forest',
        'accuracy': '86%',
        'f1_score': '55%',
        'description': 'Best overall performance, higher recall for subscription prediction'
    },
    'svm': {
        'name': 'Support Vector Machine (SVM)',
        'accuracy': '88%',
        'f1_score': '40%',
        'description': 'Good for complex decision boundaries, can be slow'
    },
    'logistic_regression': {
        'name': 'Logistic Regression',
        'accuracy': '84%',
        'f1_score': '53%',
        'description': 'Good balance, faster predictions, highly interpretable'
    },
    'neural_network': {
        'name': 'Neural Network',
        'accuracy': '85%',
        'f1_score': '54%',
        'description': 'Deep learning approach, complex patterns'
    }
}

# Check which models are available
available_models = []
for model_key, model_name in model_options.items():
    model_path = os.path.join(project_root, f'models/bank_{model_key}_model.pkl')
    if os.path.exists(model_path):
        available_models.append(model_key)

# Fallback to old naming if new naming doesn't exist
if not available_models:
    for model_key, model_name in model_options.items():
        if model_key == 'random_forest':
            old_path = os.path.join(project_root, 'models/bank_rf_model.pkl')
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
        model_path = os.path.join(project_root, f'models/bank_{model_type}_model.pkl')
        
        # Fallback to old naming convention for random forest
        if not os.path.exists(model_path) and model_type == 'random_forest':
            model_path = os.path.join(project_root, 'models/bank_rf_model.pkl')
        
        # Try scaler (updated preprocessing approach)
        scaler_path = os.path.join(project_root, 'models/bank_scaler.pkl')
        
        # Fallback to preprocessor (old approach)
        if not os.path.exists(scaler_path):
            scaler_path = os.path.join(project_root, 'models/bank_preprocessor.pkl')
        
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
st.header("🔧 Customer Information")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Demographics")
    age = st.slider("Age", 18, 95, 40)
    job = st.selectbox("Job", ["admin", "blue-collar", "entrepreneur", "housemaid", "management", 
                                "retired", "self-employed", "services", "student", "technician", "unemployed"])
    marital = st.selectbox("Marital Status", ["married", "divorced", "single"])
    education = st.selectbox("Education", ["basic.4y", "basic.6y", "basic.9y", "high.school", 
                                           "illiterate", "professional.course", "university.degree"])

with col2:
    st.subheader("Financial")
    default = st.selectbox("Has Credit in Default", ["no", "yes", "unknown"])
    housing = st.selectbox("Has Housing Loan", ["no", "yes", "unknown"])
    loan = st.selectbox("Has Personal Loan", ["no", "yes", "unknown"])
    balance = st.number_input("Account Balance", -5000, 50000, 0)

with col3:
    st.subheader("Campaign Info")
    contact = st.selectbox("Contact Method", ["cellular", "telephone"])
    month = st.selectbox("Last Contact Month", ["jan", "feb", "mar", "apr", "may", "jun", 
                                                "jul", "aug", "sep", "oct", "nov", "dec"])
    day_of_week = st.selectbox("Last Contact Day", ["mon", "tue", "wed", "thu", "fri"])
    duration = st.slider("Last Contact Duration (seconds)", 0, 3000, 180)
    campaign = st.slider("Number of Contacts in Campaign", 1, 50, 3)

# Make prediction
if st.button("Predict Subscription Likelihood", type="primary"):
    if mode == "Demo Mode":
        # Simulate prediction in demo mode
        subscription_probability = np.random.uniform(0.3, 0.7)
        subscription_likelihood = "High" if subscription_probability > 0.5 else "Low"
    else:
        # Real prediction using trained model
        try:
            # Create input DataFrame
            input_data = pd.DataFrame([{
                'age': age,
                'job': job,
                'marital': marital,
                'education': education,
                'default': default,
                'housing': housing,
                'loan': loan,
                'balance': balance,
                'contact': contact,
                'month': month,
                'day_of_week': day_of_week,
                'duration': duration,
                'campaign': campaign
            }])
            
            # Preprocess and predict
            if preprocessor:
                input_processed = preprocessor.transform(input_data)
                subscription_probability = model.predict_proba(input_processed)[0][1]
                subscription_likelihood = "High" if subscription_probability > 0.5 else "Low"
            else:
                subscription_probability = 0.5
                subscription_likelihood = "Medium"
        except Exception as e:
            st.error(f"Prediction error: {e}")
            subscription_probability = 0.5
            subscription_likelihood = "Medium"
    
    # Display results
    st.markdown("---")
    st.header("Prediction Results")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric("Subscription Probability", f"{subscription_probability:.2%}")
    
    with col2:
        likelihood_color = "🔴" if subscription_likelihood == "High" else "🟢" if subscription_likelihood == "Low" else "🟡"
        st.metric("Subscription Likelihood", f"{likelihood_color} {subscription_likelihood}")
    
    # Additional insights
    st.markdown("---")
    st.subheader("Insights")
    
    if subscription_likelihood == "High":
        st.warning("""
        **High Subscription Likelihood**
        
        This customer shows strong interest in term deposits. Consider:
        - Immediate follow-up call
        - Personalized offer presentation
        - Flexible term options
        - Competitive interest rates
        """)
    elif subscription_likelihood == "Low":
        st.success("""
        **Low Subscription Likelihood**
        
        This customer is less likely to subscribe. Consider:
        - Educational approach about benefits
        - Alternative financial products
        - Wait for better timing
        - Build relationship first
        """)
    else:
        st.info("""
        **Medium Subscription Likelihood**
        
        This customer shows moderate interest. Consider:
        - Additional information sharing
        - Trial period offers
        - Risk-free enrollment options
        - Follow-up after product changes
        """)

# Footer
st.markdown("---")
st.markdown("*Built with Streamlit and Machine Learning*")