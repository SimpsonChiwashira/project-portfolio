"""
Streamlined model training script for churn prediction.
Uses the original notebook methodology for preprocessing and training.
"""

import sys
import os
import joblib
import warnings
import argparse
import pandas as pd
import numpy as np
warnings.filterwarnings('ignore')

# Add project root to path
project_root = os.path.dirname(os.path.abspath(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from src.preprocessing.bank_preprocessing import BankDataPreprocessor
from src.preprocessing.telco_preprocessing import TelcoDataPreprocessor
from src.preprocessing.common_preprocessing import handle_imbalanced_data, train_test_split_data
from src.models.model_trainer import ModelTrainer
from src.models.model_evaluator import ModelEvaluator
from config.model_config import TelcoConfig, BankConfig

# Parse command line arguments
parser = argparse.ArgumentParser(description='Train churn prediction models')
parser.add_argument('--skip-svm', action='store_true', help='Skip SVM training (faster)')
parser.add_argument('--skip-nn', action='store_true', help='Skip Neural Network training (faster)')
parser.add_argument('--quick', action='store_true', help='Quick mode: only train Random Forest and Logistic Regression')
args = parser.parse_args()

print("=" * 60)
print("CHURN PREDICTION MODEL TRAINING")
print("=" * 60)

# Check TensorFlow availability
try:
    import tensorflow as tf
    TENSORFLOW_AVAILABLE = True
    print("TensorFlow available. Neural network training enabled.")
except ImportError:
    TENSORFLOW_AVAILABLE = False
    print("TensorFlow not available. Neural network training will be disabled.")

# Train Bank Marketing Model
print("\n" + "=" * 60)
print("Training Bank Marketing Churn Prediction Models")
print("=" * 60)

try:
    # 1. Load and preprocess data using original notebook methodology
    print("\n1. Loading and preprocessing data (original methodology)...")
    bank_preprocessor = BankDataPreprocessor()
    X, y = bank_preprocessor.preprocess_pipeline(BankConfig.DATA_PATH)
    print(f"   Data loaded: {X.shape[0]} samples, {X.shape[1]} features")
    
    # 2. Split data
    print("\n2. Splitting data...")
    X_train, X_test, y_train, y_test = train_test_split_data(
        X, y, test_size=BankConfig.TEST_SIZE, random_state=BankConfig.RANDOM_STATE
    )
    
    # 3. Handle class imbalance
    print("\n3. Handling class imbalance...")
    X_train_resampled, y_train_resampled = handle_imbalanced_data(
        X_train, y_train, method=BankConfig.BALANCE_METHOD, random_state=BankConfig.RANDOM_STATE
    )
    
    # 4. Train multiple models
    print("\n4. Training multiple models...")
    trainer = ModelTrainer(random_state=BankConfig.RANDOM_STATE)
    evaluator = ModelEvaluator()
    
    models_trained = {}
    
    # Random Forest
    print("\n   a) Training Random Forest model...")
    rf_model = trainer.train_random_forest(
        X_train_resampled, y_train_resampled,
        **BankConfig.RF_PARAMS
    )
    rf_metrics = evaluator.evaluate_model(
        rf_model, X_test, y_test,
        model_name="Bank Random Forest"
    )
    models_trained['random_forest'] = rf_model
    
    # Logistic Regression (faster than SVM)
    print("\n   b) Training Logistic Regression model...")
    try:
        lr_model = trainer.train_logistic_regression(
            X_train_resampled, y_train_resampled
        )
        lr_metrics = evaluator.evaluate_model(
            lr_model, X_test, y_test,
            model_name="Bank Logistic Regression"
        )
        models_trained['logistic_regression'] = lr_model
    except Exception as e:
        print(f"   Logistic Regression training failed: {e}")
    
    # SVM (slower but important for research completeness)
    if not args.skip_svm and not args.quick:
        print("\n   c) Training SVM model (this may take a while)...")
        try:
            svm_model = trainer.train_svm(
                X_train_resampled, y_train_resampled,
                **BankConfig.SVM_PARAMS
            )
            svm_metrics = evaluator.evaluate_model(
                svm_model, X_test, y_test,
                model_name="Bank SVM"
            )
            models_trained['svm'] = svm_model
        except Exception as e:
            print(f"   SVM training failed: {e}")
    else:
        print("\n   c) Skipping SVM (use --skip-svm flag to skip)")
    
    # Neural Network (now that TensorFlow is available)
    if not args.skip_nn and not args.quick and TENSORFLOW_AVAILABLE:
        print("\n   d) Training Neural Network model...")
        try:
            nn_model, nn_history = trainer.train_neural_network(
                X_train_resampled, y_train_resampled,
                input_dim=X_train_resampled.shape[1],
                **BankConfig.NN_PARAMS
            )
            nn_metrics = evaluator.evaluate_model(
                nn_model, X_test, y_test,
                model_name="Bank Neural Network"
            )
            models_trained['neural_network'] = nn_model
        except Exception as e:
            print(f"   Neural Network training failed: {e}")
    else:
        if not TENSORFLOW_AVAILABLE:
            print("\n   d) Skipping Neural Network (TensorFlow not available)")
        else:
            print("\n   d) Skipping Neural Network (use --skip-nn flag to skip)")
    
    # 5. Save models and preprocessor
    print("\n5. Saving models and preprocessor...")
    os.makedirs('models', exist_ok=True)
    
    # Save each model
    for model_name, model in models_trained.items():
        model_path = f'models/bank_{model_name}_model.pkl'
        joblib.dump(model, model_path)
        print(f"   {model_name} saved to: {model_path}")
    
    # Save preprocessor (scaler)
    if bank_preprocessor.scaler:
        joblib.dump(bank_preprocessor.scaler, 'models/bank_scaler.pkl')
        print("   Scaler saved to: models/bank_scaler.pkl")
    
    # Save feature columns
    joblib.dump(bank_preprocessor.feature_columns, 'models/bank_feature_columns.pkl')
    
    print("\n" + "=" * 60)
    print("Bank model training completed successfully!")
    print(f"Models trained: {list(models_trained.keys())}")
    print("=" * 60)
    
    BANK_SUCCESS = True
except Exception as e:
    print(f"\nBank model training failed: {e}")
    BANK_SUCCESS = False

# Train Telco Churn Model
print("\n" + "=" * 60)
print("Training Telco Churn Prediction Models")
print("=" * 60)

try:
    # 1. Load and preprocess data using original notebook methodology
    print("\n1. Loading and preprocessing data (original methodology)...")
    telco_preprocessor = TelcoDataPreprocessor()
    X, y = telco_preprocessor.preprocess_pipeline(TelcoConfig.DATA_PATH)
    print(f"   Data loaded: {X.shape[0]} samples, {X.shape[1]} features")
    
    # 2. Split data
    print("\n2. Splitting data...")
    X_train, X_test, y_train, y_test = train_test_split_data(
        X, y, test_size=TelcoConfig.TEST_SIZE, random_state=TelcoConfig.RANDOM_STATE
    )
    
    # 3. Handle class imbalance
    print("\n3. Handling class imbalance...")
    X_train_resampled, y_train_resampled = handle_imbalanced_data(
        X_train, y_train, method=TelcoConfig.BALANCE_METHOD, random_state=TelcoConfig.RANDOM_STATE
    )
    
    # 4. Train multiple models
    print("\n4. Training multiple models...")
    trainer = ModelTrainer(random_state=TelcoConfig.RANDOM_STATE)
    evaluator = ModelEvaluator()
    
    models_trained = {}
    
    # Random Forest
    print("\n   a) Training Random Forest model...")
    rf_model = trainer.train_random_forest(
        X_train_resampled, y_train_resampled,
        **TelcoConfig.RF_PARAMS
    )
    rf_metrics = evaluator.evaluate_model(
        rf_model, X_test, y_test,
        model_name="Telco Random Forest"
    )
    models_trained['random_forest'] = rf_model
    
    # Logistic Regression (faster than SVM)
    print("\n   b) Training Logistic Regression model...")
    try:
        lr_model = trainer.train_logistic_regression(
            X_train_resampled, y_train_resampled
        )
        lr_metrics = evaluator.evaluate_model(
            lr_model, X_test, y_test,
            model_name="Telco Logistic Regression"
        )
        models_trained['logistic_regression'] = lr_model
    except Exception as e:
        print(f"   Logistic Regression training failed: {e}")
    
    # SVM (slower but important for research completeness)
    if not args.skip_svm and not args.quick:
        print("\n   c) Training SVM model (this may take a while)...")
        try:
            svm_model = trainer.train_svm(
                X_train_resampled, y_train_resampled,
                **TelcoConfig.SVM_PARAMS
            )
            svm_metrics = evaluator.evaluate_model(
                svm_model, X_test, y_test,
                model_name="Telco SVM"
            )
            models_trained['svm'] = svm_model
        except Exception as e:
            print(f"   SVM training failed: {e}")
    else:
        print("\n   c) Skipping SVM (use --skip-svm flag to skip)")
    
    # Neural Network (now that TensorFlow is available)
    if not args.skip_nn and not args.quick and TENSORFLOW_AVAILABLE:
        print("\n   d) Training Neural Network model...")
        try:
            nn_model, nn_history = trainer.train_neural_network(
                X_train_resampled, y_train_resampled,
                input_dim=X_train_resampled.shape[1],
                **TelcoConfig.NN_PARAMS
            )
            nn_metrics = evaluator.evaluate_model(
                nn_model, X_test, y_test,
                model_name="Telco Neural Network"
            )
            models_trained['neural_network'] = nn_model
        except Exception as e:
            print(f"   Neural Network training failed: {e}")
    else:
        if not TENSORFLOW_AVAILABLE:
            print("\n   d) Skipping Neural Network (TensorFlow not available)")
        else:
            print("\n   d) Skipping Neural Network (use --skip-nn flag to skip)")
    
    # 5. Save models and preprocessor
    print("\n5. Saving models and preprocessor...")
    os.makedirs('models', exist_ok=True)
    
    # Save each model
    for model_name, model in models_trained.items():
        model_path = f'models/telco_{model_name}_model.pkl'
        joblib.dump(model, model_path)
        print(f"   {model_name} saved to: {model_path}")
    
    # Save preprocessor (scaler)
    if telco_preprocessor.scaler:
        joblib.dump(telco_preprocessor.scaler, 'models/telco_scaler.pkl')
        print("   Scaler saved to: models/telco_scaler.pkl")
    
    # Save feature columns
    joblib.dump(telco_preprocessor.feature_columns, 'models/telco_feature_columns.pkl')
    
    print("\n" + "=" * 60)
    print("Telco model training completed successfully!")
    print(f"Models trained: {list(models_trained.keys())}")
    print("=" * 60)
    
    TELCO_SUCCESS = True
except Exception as e:
    print(f"\nTelco model training failed: {e}")
    TELCO_SUCCESS = False

# Summary
print("\n" + "=" * 60)
print("TRAINING SUMMARY")
print("=" * 60)
print(f"Bank Marketing Model: {'[SUCCESS]' if BANK_SUCCESS else '[FAILED]'}")
print(f"Telco Churn Model: {'[SUCCESS]' if TELCO_SUCCESS else '[FAILED]'}")
print("=" * 60)

if BANK_SUCCESS and TELCO_SUCCESS:
    print("\n[SUCCESS] All models trained successfully!")
    print("Using original notebook methodology for preprocessing.")
    print("You can now run the Streamlit apps with full ML functionality.")
    print("Run: python run_app.py")
else:
    print("\n[PARTIAL SUCCESS] Some models failed to train.")
    print("Check the error messages above for details.")