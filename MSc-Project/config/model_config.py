"""
Model configuration parameters for churn prediction.
"""

class TelcoConfig:
    """Configuration parameters for Telco Churn prediction."""
    
    # Data paths
    DATA_PATH = 'data/raw/telco.csv'
    PROCESSED_DATA_PATH = 'data/processed/Telco-New.csv'
    
    # Random state for reproducibility
    RANDOM_STATE = 42
    
    # Model parameters
    RF_PARAMS = {
        'n_estimators': 100,
        'max_depth': 10,
        'min_samples_split': 5,
        'min_samples_leaf': 2,
        'random_state': 42,
        'n_jobs': -1
    }
    
    SVM_PARAMS = {
        'C': 1.0,
        'kernel': 'rbf',
        'gamma': 'scale'
    }
    
    LR_PARAMS = {
        'C': 1.0,
        'max_iter': 1000,
        'random_state': 42,
        'n_jobs': -1
    }
    
    NN_PARAMS = {
        'hidden_layers': (64, 32),
        'dropout_rate': 0.3,
        'learning_rate': 0.001,
        'epochs': 50,
        'batch_size': 32
    }
    
    # Test size for train-test split
    TEST_SIZE = 0.2
    
    # Class imbalance handling method
    BALANCE_METHOD = 'smote'  # 'smote', 'undersample', 'none'


class BankConfig:
    """Configuration parameters for Bank Marketing prediction."""
    
    # Data paths
    DATA_PATH = 'data/raw/bank-full.csv'
    PROCESSED_DATA_PATH = 'data/processed/Bank-Full-New.csv'
    
    # Random state for reproducibility
    RANDOM_STATE = 42
    
    # Model parameters
    RF_PARAMS = {
        'n_estimators': 100,
        'max_depth': 15,
        'min_samples_split': 10,
        'min_samples_leaf': 2,
        'random_state': 42,
        'n_jobs': -1
    }
    
    SVM_PARAMS = {
        'C': 1.0,
        'kernel': 'rbf',
        'gamma': 'scale'
    }
    
    LR_PARAMS = {
        'C': 1.0,
        'max_iter': 1000,
        'random_state': 42,
        'n_jobs': -1
    }
    
    NN_PARAMS = {
        'hidden_layers': (64, 32),
        'dropout_rate': 0.3,
        'learning_rate': 0.001,
        'epochs': 50,
        'batch_size': 32
    }
    
    # Test size for train-test split
    TEST_SIZE = 0.2
    
    # Class imbalance handling method
    BALANCE_METHOD = 'smote'  # 'smote', 'undersample', 'none'