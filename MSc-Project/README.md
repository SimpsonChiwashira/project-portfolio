# Customer Churn Prediction Suite

An Evaluation of Supervised Learning Models in the Prediction and Analysis of Customer Churn

## 📊 Abstract

This study investigates the effectiveness of supervised learning models in predicting and analysing customer churn within the Telecommunications and Banking Marketing sectors. Utilising sector-specific datasets, the research explores imbalanced data handling techniques, employing both Random Undersampling and SMOTE to achieve balanced class representation. Evaluation of Support Vector Machines, Artificial Neural Networks, and Random Forests, post-hyperparameter tuning, identifies Random Forests as the optimal classifier across all datasets. The study emphasises the impact of resampling techniques on classifier performance pre- and post-model refinement, recommending the utilisation of Random Forests for predictive accuracy in such sectors.

## 🚀 Quick Start

### Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd msc-acs-project
   ```

2. **Create virtual environment:**
   ```bash
   # Using conda (recommended)
   conda env create -f environment.yml
   conda activate churn-prediction
   
   # Or using pip
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Run the Streamlit applications:**
   ```bash
   streamlit run deployment/streamlit/home.py
   ```

## 📁 Project Structure

```
msc-acs-project/
├── data/                      # Data storage
│   ├── raw/                   # Original datasets
│   │   ├── bank-full.csv
│   │   └── telco.csv
│   └── processed/             # Processed datasets
│       ├── Bank-Full-New.csv
│       └── Telco-New.csv
├── notebooks/                 # Jupyter notebooks (original research)
│   ├── banking/               # Banking analysis
│   │   └── Bank-Notebook.ipynb
│   └── telco/                # Telco analysis
│       └── Telco-Notebook.ipynb
├── src/                      # Source code (modular structure)
│   ├── models/              # Model training & evaluation
│   │   ├── model_trainer.py
│   │   ├── model_evaluator.py
│   │   └── hyperparameter_tuning.py
│   ├── preprocessing/       # Data preprocessing (matches notebooks)
│   │   ├── bank_preprocessing.py
│   │   ├── telco_preprocessing.py
│   │   └── common_preprocessing.py
│   └── utils/               # Utility functions
│       ├── visualization.py
│       ├── data_loader.py
│       └── model_utils.py
├── deployment/              # Deployment configurations
│   ├── streamlit/          # Streamlit applications (recommended)
│   │   ├── home.py
│   │   └── pages/
│   │       ├── telco_churn_app.py
│   │       └── bank_churn_app.py
│   └── flask/              # Flask applications (original)
│       ├── telco/         # Original Telco Flask app
│       └── bank/          # Original Bank Flask app
├── models/                 # Trained models (gitignored)
├── original/              # Original work for reference
├── config/                # Configuration files
├── requirements.txt        # Python dependencies
├── environment.yml         # Conda environment
├── train_models.py        # Automated model training
├── run_app.py            # Streamlit app launcher
├── TRAINING_OPTIONS.md    # Training guide
└── README.md              # This file
```

## 🎯 Applications

### Deployment Options

This project supports **two deployment frameworks**:

#### 1. Streamlit Applications (Recommended)
- **Modern, interactive UI** with real-time predictions
- **Model selection** - Switch between Random Forest, SVM, Logistic Regression, and Neural Network
- **Dark theme** with clean, professional design
- **Dynamic model information** showing performance metrics for each algorithm

#### 2. Flask Applications (Original Implementation)
- **Original research implementation** preserved for reference
- **HTML-based templates** with custom styling
- **Single model per app** (Random Forest)
- **Legacy deployment** - maintained for research consistency

### Running Streamlit Applications

```bash
# Quick start
python run_app.py

# Or manually
streamlit run deployment/streamlit/home.py
```

**Individual Apps:**
```bash
# Telco Churn App
streamlit run deployment/streamlit/pages/telco_churn_app.py

# Bank Marketing App
streamlit run deployment/streamlit/pages/bank_churn_app.py
```

### Running Flask Applications

```bash
# Telco Churn App
cd deployment/flask/telco
python app.py

# Bank Marketing App  
cd deployment/flask/bank
python app.py
```

### Application Details

#### Telco Churn Prediction
- **Input**: Customer demographics, service subscriptions, usage patterns
- **Output**: Churn probability and risk assessment
- **Models**: Random Forest, SVM, Logistic Regression, Neural Network
- **Performance**: ~80% accuracy, ~61% F1-Score (Random Forest)

#### Bank Marketing Prediction
- **Input**: Customer demographics, campaign interactions, financial data
- **Output**: Subscription likelihood for term deposits
- **Models**: Random Forest, SVM, Logistic Regression, Neural Network
- **Performance**: ~86% accuracy, ~55% F1-Score (Random Forest)

## 🔧 Usage

### Quick Start with Streamlit (Recommended)

```bash
# Launch the Streamlit home page
python run_app.py

# Or run directly
streamlit run deployment/streamlit/home.py
```

### Running Original Flask Applications

```bash
# Telco Churn App
cd deployment/flask/telco
python app.py

# Bank Marketing App  
cd deployment/flask/bank
python app.py
```

### Training Models

#### Option 1: Using Original Notebooks (Recommended for Research)

```bash
# Open the comprehensive research notebooks
jupyter notebook notebooks/banking/Bank-Notebook.ipynb
jupyter notebook notebooks/telco/Telco-Notebook.ipynb

# Run cells sequentially to:
# - Load and preprocess data (original methodology)
# - Handle class imbalance with SMOTE
# - Train and evaluate multiple models
# - Perform hyperparameter tuning
# - Save trained models
```

#### Option 2: Using Automated Training Script

```bash
# Quick training (Random Forest + Logistic Regression only)
python train_models.py --quick

# Full training (all 4 models)
python train_models.py

# Skip SVM (faster)
python train_models.py --skip-svm

# Skip Neural Network (faster)
python train_models.py --skip-nn
```

See `TRAINING_OPTIONS.md` for detailed training options.

### Using Python Modules

```python
from src.preprocessing.telco_preprocessing import TelcoDataPreprocessor
from src.models.model_trainer import ModelTrainer
from src.models.model_evaluator import ModelEvaluator

# Load and preprocess data (matches original notebook methodology)
preprocessor = TelcoDataPreprocessor()
X, y = preprocessor.preprocess_pipeline('data/raw/telco.csv')

# Train model
trainer = ModelTrainer()
model = trainer.train_random_forest(X, y)

# Evaluate model
evaluator = ModelEvaluator()
metrics = evaluator.evaluate_model(model, X_test, y_test, "Telco Random Forest")
```

## 📊 Model Performance

### Telco Dataset
| Model | Accuracy | Precision | Recall | F1-Score | ROC-AUC |
|-------|----------|-----------|--------|----------|---------|
| Random Forest | 0.80 | 0.65 | 0.50 | 0.56 | 0.84 |
| SVM | 0.76 | 0.52 | 0.45 | 0.48 | 0.80 |
| Neural Network | 0.78 | 0.58 | 0.42 | 0.49 | 0.82 |

### Bank Dataset
| Model | Accuracy | Precision | Recall | F1-Score | ROC-AUC |
|-------|----------|-----------|--------|----------|---------|
| Random Forest | 0.90 | 0.62 | 0.38 | 0.47 | 0.89 |
| SVM | 0.88 | 0.55 | 0.32 | 0.40 | 0.85 |
| Neural Network | 0.89 | 0.58 | 0.35 | 0.44 | 0.87 |

## 🔬 Research Findings

### Key Insights

1. **Random Forest Superiority**: Random Forest consistently outperformed other models across both datasets
2. **Imbalance Handling**: SMOTE and Random Undersampling significantly improved model performance
3. **Feature Importance**: Duration of contact and previous campaign outcomes were top predictors
4. **Overfitting Mitigation**: Proper hyperparameter tuning was essential for neural networks

### Data Imbalance Impact

- **Original Data**: 11.7% churn rate (telco), 11.3% subscription rate (bank)
- **After SMOTE**: Balanced 50/50 class distribution
- **Performance Improvement**: 15-20% F1-Score improvement with balanced data

## 🛠️ Technical Stack

- **Python 3.9+**: Core programming language
- **Streamlit**: Web application framework
- **Scikit-Learn**: Machine learning library
- **TensorFlow/Keras**: Deep learning framework
- **Pandas/NumPy**: Data manipulation
- **Matplotlib/Seaborn**: Data visualization
- **Imbalanced-Learn**: SMOTE and undersampling techniques

## 📝 Dependencies

See `requirements.txt` for complete list of dependencies:

```
pandas>=1.4.4
numpy>=1.19.5
scikit-learn>=0.24.2
tensorflow>=2.8.0
streamlit>=1.20.0
imbalanced-learn>=0.8.0
matplotlib>=3.4.0
seaborn>=0.11.0
```

## 🧪 Testing

Run unit tests (if available):

```bash
python -m pytest tests/
```

## 📈 Model Training Pipeline

1. **Data Loading**: Load raw datasets from `data/raw/`
2. **Preprocessing**: Clean, encode, and scale features
3. **Imbalance Handling**: Apply SMOTE or undersampling
4. **Model Training**: Train multiple algorithms
5. **Hyperparameter Tuning**: Optimize model parameters
6. **Evaluation**: Compare models using multiple metrics
7. **Deployment**: Save best models for production use

## 🎓 Academic Context

This project was developed as part of an MSc in Advanced Computer Science dissertation focusing on:

- **Customer Relationship Management (CRM)**
- **Predictive Analytics**
- **Imbalanced Learning**
- **Machine Learning Interpretability**

## 👤 Author

**Simpson Chiwashira**
- MSc Advanced Computer Science
- Email: simpsonchiwasira@icloud.com

## 📄 License

This project is for educational and research purposes. Please cite appropriately if used in academic work.

## 🤝 Contributing

This is a research project, but suggestions and improvements are welcome. Please feel free to open issues or submit pull requests.

## ⚠️ Disclaimer

Predictions generated by these applications are for informational purposes only and should not be used as the sole basis for business decisions. Always consider additional business context, regulatory requirements, and human judgment when making customer retention or marketing decisions.

## 📞 Support

For questions or issues related to this project, please contact:
- Email: simpsonchiwasira@icloud.com
- GitHub Issues: (if repository is public)

---

*Built with ❤️ using Streamlit and Scikit-Learn*