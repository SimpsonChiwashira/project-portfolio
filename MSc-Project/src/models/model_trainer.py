"""
Model training module for churn prediction.
"""

import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import joblib
import warnings
warnings.filterwarnings('ignore')


class ModelTrainer:
    """Class for training machine learning models."""
    
    def __init__(self, random_state=42):
        """
        Initialize the ModelTrainer.
        
        Args:
            random_state: Random seed for reproducibility
        """
        self.random_state = random_state
    
    def train_random_forest(self, X_train, y_train, n_estimators=100, max_depth=15, 
                           min_samples_split=10, min_samples_leaf=2, n_jobs=-1):
        """
        Train a Random Forest classifier.
        
        Args:
            X_train: Training features
            y_train: Training labels
            n_estimators: Number of trees in the forest
            max_depth: Maximum depth of trees
            min_samples_split: Minimum samples required to split
            min_samples_leaf: Minimum samples in leaf nodes
            n_jobs: Number of parallel jobs
            
        Returns:
            Trained Random Forest model
        """
        rf_model = RandomForestClassifier(
            n_estimators=n_estimators,
            max_depth=max_depth,
            min_samples_split=min_samples_split,
            min_samples_leaf=min_samples_leaf,
            random_state=self.random_state,
            n_jobs=n_jobs
        )
        
        rf_model.fit(X_train, y_train)
        print(f"Random Forest trained with parameters: {rf_model.get_params()}")
        return rf_model
    
    def train_logistic_regression(self, X_train, y_train, C=1.0, max_iter=1000, n_jobs=-1):
        """
        Train a Logistic Regression classifier.
        
        Args:
            X_train: Training features
            y_train: Training labels
            C: Regularization parameter
            max_iter: Maximum iterations
            n_jobs: Number of parallel jobs
            
        Returns:
            Trained Logistic Regression model
        """
        lr_model = LogisticRegression(
            C=C,
            max_iter=max_iter,
            random_state=self.random_state,
            n_jobs=n_jobs
        )
        
        lr_model.fit(X_train, y_train)
        print(f"Logistic Regression trained with parameters: {lr_model.get_params()}")
        return lr_model
    
    def train_svm(self, X_train, y_train, C=1.0, kernel='rbf', gamma='scale'):
        """
        Train a Support Vector Machine classifier.
        
        Args:
            X_train: Training features
            y_train: Training labels
            C: Regularization parameter
            kernel: Kernel type ('linear', 'rbf', 'poly')
            gamma: Kernel coefficient
            
        Returns:
            Trained SVM model
        """
        svm_model = SVC(
            C=C,
            kernel=kernel,
            gamma=gamma,
            probability=True,
            random_state=self.random_state
        )
        
        svm_model.fit(X_train, y_train)
        print(f"SVM trained with parameters: {svm_model.get_params()}")
        return svm_model
    
    def train_neural_network(self, X_train, y_train, input_dim, hidden_layers=(64, 32), 
                            dropout_rate=0.3, learning_rate=0.001, epochs=50, batch_size=32):
        """
        Train a Neural Network classifier using TensorFlow/Keras.
        
        Args:
            X_train: Training features
            y_train: Training labels
            input_dim: Number of input features
            hidden_layers: Tuple of hidden layer sizes
            dropout_rate: Dropout rate for regularization
            learning_rate: Learning rate for optimizer
            epochs: Number of training epochs
            batch_size: Batch size for training
            
        Returns:
            Trained Neural Network model and training history
        """
        # Build the neural network
        model = keras.Sequential()
        
        # Input layer
        model.add(layers.Dense(hidden_layers[0], input_dim=input_dim, activation='relu'))
        model.add(layers.Dropout(dropout_rate))
        
        # Hidden layers
        for units in hidden_layers[1:]:
            model.add(layers.Dense(units, activation='relu'))
            model.add(layers.Dropout(dropout_rate))
        
        # Output layer
        model.add(layers.Dense(1, activation='sigmoid'))
        
        # Compile the model
        optimizer = keras.optimizers.Adam(learning_rate=learning_rate)
        model.compile(
            optimizer=optimizer,
            loss='binary_crossentropy',
            metrics=['accuracy']
        )
        
        # Train the model
        history = model.fit(
            X_train, y_train,
            epochs=epochs,
            batch_size=batch_size,
            verbose=0,
            validation_split=0.2
        )
        
        print(f"Neural Network trained with {epochs} epochs")
        return model, history