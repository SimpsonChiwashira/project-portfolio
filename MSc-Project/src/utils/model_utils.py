"""
Model utility functions for saving and loading models.
"""

import joblib
import os
import warnings
warnings.filterwarnings('ignore')


def save_model(model, file_path):
    """
    Save a trained model to disk.
    
    Args:
        model: Trained model to save
        file_path: Path to save the model
    """
    # Create directory if it doesn't exist
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    joblib.dump(model, file_path)
    print(f"Model saved to: {file_path}")


def load_model(file_path):
    """
    Load a trained model from disk.
    
    Args:
        file_path: Path to load the model from
        
    Returns:
        Loaded model
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Model file not found: {file_path}")
    
    model = joblib.load(file_path)
    print(f"Model loaded from: {file_path}")
    
    return model