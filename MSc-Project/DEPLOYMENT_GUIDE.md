# Deployment Guide

This project supports **two deployment frameworks** to give you flexibility in how you use your churn prediction models.

## 🚀 Deployment Options

### Option 1: Streamlit Applications (Recommended)

**Best for:** Interactive demos, presentations, and modern web interfaces

**Features:**
- ✅ Modern, interactive UI with real-time predictions
- ✅ Model selection (switch between Random Forest, SVM, Logistic Regression, Neural Network)
- ✅ Dark theme with clean, professional design
- ✅ Dynamic model information showing performance metrics
- ✅ Responsive design that works on all devices

**How to Run:**
```bash
# Quick start
python run_app.py

# Or manually
streamlit run deployment/streamlit/home.py
```

**Access Points:**
- Home Page: `http://localhost:8501`
- Telco Churn App: Available from home page navigation or directly via `pages/telco_churn_app.py`
- Bank Marketing App: Available from home page navigation or directly via `pages/bank_churn_app.py`

**Individual Apps:**
```bash
# Telco Churn App
streamlit run deployment/streamlit/pages/telco_churn_app.py

# Bank Marketing App
streamlit run deployment/streamlit/pages/bank_churn_app.py
```

**File Naming:**
- Clean file names without emojis
- `telco_churn_app.py` and `bank_churn_app.py`
- Home page: `home.py`

### Option 2: Flask Applications (Original Implementation)

**Best for:** Research consistency, legacy deployment, custom web integration

**Features:**
- ✅ Original research implementation preserved
- ✅ HTML-based templates with custom styling
- ✅ Single model per app (Random Forest - matches original research)
- ✅ Lightweight deployment
- ✅ Easy integration with existing web infrastructure

**How to Run:**
```bash
# Telco Churn App
cd deployment/flask/telco
python app.py

# Bank Marketing App  
cd deployment/flask/bank
python app.py
```

**Access Points:**
- Telco Churn App: `http://localhost:5000`
- Bank Marketing App: `http://localhost:5001` (if configured separately)

## 🔄 Comparison

| Feature | Streamlit | Flask |
|---------|-----------|-------|
| **UI Framework** | Modern Python framework | Traditional web framework |
| **Model Selection** | ✅ 4 models | ❌ 1 model (RF) |
| **Interactivity** | ✅ Real-time updates | ❌ Form-based |
| **Mobile Friendly** | ✅ Responsive | ❌ Fixed layout |
| **Customization** | ⚠️ Limited to Streamlit components | ✅ Full HTML/CSS control |
| **Ease of Use** | ✅ Very easy | ⚠️ Requires web dev knowledge |
| **Research Consistency** | ⚠️ Updated approach | ✅ Original methodology |

## 📊 Model Compatibility

### Streamlit Apps
- ✅ Works with models trained using either methodology
- ✅ Automatically detects available models
- ✅ Fallback to demo mode if models not found
- ✅ Supports both old and new preprocessing approaches

### Flask Apps
- ✅ Uses original pickle models
- ✅ Exact methodology from original research
- ✅ No modifications needed

## 🎯 When to Use Each

### Use Streamlit When:
- Giving presentations or demos
- Need interactive model comparison
- Want modern, polished UI
- Deploying for non-technical users
- Need mobile-friendly interface

### Use Flask When:
- Maintaining research consistency
- Integrating with existing web infrastructure
- Need custom HTML/CSS styling
- Lightweight deployment is required
- Want exact original implementation

## 🔧 Configuration

### Streamlit Configuration
Edit `.streamlit/config.toml` for Streamlit-specific settings:
```toml
[theme]
primaryColor = "#1f77b4"
backgroundColor = "#ffffff"
secondaryBackgroundColor = "#f0f2f6"
```

### Flask Configuration
Edit `deployment/flask/*/app.py` for Flask-specific settings:
```python
app.run(debug=True, port=5000)
```

## 🐳 Docker Deployment (Optional)

### Streamlit Docker
```dockerfile
FROM python:3.10
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["streamlit", "run", "deployment/streamlit/home.py"]
```

### Flask Docker
```dockerfile
FROM python:3.10
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY deployment/flask/telco ./app
CMD ["python", "app.py"]
```

## 🚀 Production Deployment

### Streamlit Deployment Options:
1. **Streamlit Cloud** - Free hosting for Streamlit apps
2. **Heroku** - Platform as a service
3. **AWS/Azure/GCP** - Cloud hosting
4. **Docker** - Containerized deployment

### Flask Deployment Options:
1. **Gunicorn** - Production WSGI server
2. **Nginx** - Reverse proxy
3. **Docker** - Containerized deployment
4. **Cloud platforms** - Various hosting options

## 📝 Notes

- **Streamlit apps** are recommended for most use cases due to ease of use and modern features
- **Flask apps** are preserved for research consistency and reference
- Both approaches use the same trained models
- Model training methodology is preserved in the Jupyter notebooks
- The modular source code structure makes it easy to extend either framework

## 🆘 Troubleshooting

### Streamlit Issues:
- **Port already in use:** Change port with `streamlit run --server.port 8502`
- **Models not loading:** Check model paths in `models/` directory
- **Navigation issues:** Ensure file paths are correct in `st.switch_page()`

### Flask Issues:
- **Template not found:** Check template paths in Flask app
- **Model loading errors:** Verify pickle file paths
- **Port conflicts:** Change port in `app.run()`

## 📞 Support

For issues or questions:
1. Check the original notebooks for methodology
2. Review the `TRAINING_OPTIONS.md` for model training
3. Refer to this guide for deployment options
4. Test both frameworks to choose the best fit for your needs