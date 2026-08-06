"""
Common preprocessing functions for both datasets.
"""

import numpy as np
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE
from imblearn.under_sampling import RandomUnderSampler
import warnings
warnings.filterwarnings('ignore')


def train_test_split_data(X, y, test_size=0.2, random_state=42):
    """
    Split data into training and testing sets.
    
    Args:
        X: Features
        y: Target variable
        test_size: Proportion of data for testing
        random_state: Random seed for reproducibility
        
    Returns:
        X_train, X_test, y_train, y_test
    """
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=y
    )
    
    print(f"Training set size: {X_train.shape[0]}")
    print(f"Testing set size: {X_test.shape[0]}")
    
    return X_train, X_test, y_train, y_test


def handle_imbalanced_data(X_train, y_train, method='smote', random_state=42):
    """
    Handle imbalanced data using oversampling or undersampling.
    
    Args:
        X_train: Training features
        y_train: Training labels
        method: Method to use ('smote', 'undersample', 'none')
        random_state: Random seed for reproducibility
        
    Returns:
        Resampled X_train, y_train
    """
    from collections import Counter
    
    print(f"Original class distribution: {Counter(y_train)}")
    
    if method == 'smote':
        # Use SMOTE for oversampling
        smote = SMOTE(random_state=random_state)
        X_train_resampled, y_train_resampled = smote.fit_resample(X_train, y_train)
        print(f"After SMOTE: {Counter(y_train_resampled)}")
        
    elif method == 'undersample':
        # Use Random Undersampling
        undersampler = RandomUnderSampler(random_state=random_state)
        X_train_resampled, y_train_resampled = undersampler.fit_resample(X_train, y_train)
        print(f"After Undersampling: {Counter(y_train_resampled)}")
        
    else:
        # No resampling
        X_train_resampled, y_train_resampled = X_train, y_train
        print("No resampling applied")
    
    return X_train_resampled, y_train_resampled