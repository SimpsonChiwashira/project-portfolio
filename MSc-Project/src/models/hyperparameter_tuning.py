"""
Hyperparameter tuning module for churn prediction.
"""

from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
import numpy as np
import warnings
warnings.filterwarnings('ignore')


class HyperparameterTuner:
    """Class for hyperparameter tuning of machine learning models."""
    
    def __init__(self, random_state=42):
        """
        Initialize the HyperparameterTuner.
        
        Args:
            random_state: Random seed for reproducibility
        """
        self.random_state = random_state
    
    def tune_random_forest(self, X_train, y_train, cv=5, n_iter=50):
        """
        Tune Random Forest hyperparameters using RandomizedSearchCV.
        
        Args:
            X_train: Training features
            y_train: Training labels
            cv: Number of cross-validation folds
            n_iter: Number of parameter settings sampled
            
        Returns:
            Best Random Forest model and best parameters
        """
        param_distributions = {
            'n_estimators': [50, 100, 200, 300],
            'max_depth': [10, 15, 20, 25, None],
            'min_samples_split': [2, 5, 10],
            'min_samples_leaf': [1, 2, 4],
            'max_features': ['sqrt', 'log2']
        }
        
        rf = RandomForestClassifier(random_state=self.random_state, n_jobs=-1)
        
        random_search = RandomizedSearchCV(
            rf, param_distributions, n_iter=n_iter, cv=cv,
            random_state=self.random_state, n_jobs=-1, verbose=1
        )
        
        random_search.fit(X_train, y_train)
        
        print(f"Best Random Forest parameters: {random_search.best_params_}")
        return random_search.best_estimator_, random_search.best_params_
    
    def tune_svm(self, X_train, y_train, cv=5, n_iter=20):
        """
        Tune SVM hyperparameters using RandomizedSearchCV.
        
        Args:
            X_train: Training features
            y_train: Training labels
            cv: Number of cross-validation folds
            n_iter: Number of parameter settings sampled
            
        Returns:
            Best SVM model and best parameters
        """
        param_distributions = {
            'C': [0.1, 1, 10, 100],
            'kernel': ['linear', 'rbf', 'poly'],
            'gamma': ['scale', 'auto', 0.001, 0.01, 0.1, 1]
        }
        
        svm = SVC(random_state=self.random_state, probability=True)
        
        random_search = RandomizedSearchCV(
            svm, param_distributions, n_iter=n_iter, cv=cv,
            random_state=self.random_state, n_jobs=-1, verbose=1
        )
        
        random_search.fit(X_train, y_train)
        
        print(f"Best SVM parameters: {random_search.best_params_}")
        return random_search.best_estimator_, random_search.best_params_
    
    def tune_logistic_regression(self, X_train, y_train, cv=5):
        """
        Tune Logistic Regression hyperparameters using GridSearchCV.
        
        Args:
            X_train: Training features
            y_train: Training labels
            cv: Number of cross-validation folds
            
        Returns:
            Best Logistic Regression model and best parameters
        """
        param_grid = {
            'C': [0.01, 0.1, 1, 10, 100],
            'solver': ['liblinear', 'lbfgs'],
            'max_iter': [100, 500, 1000]
        }
        
        lr = LogisticRegression(random_state=self.random_state, n_jobs=-1)
        
        grid_search = GridSearchCV(
            lr, param_grid, cv=cv, n_jobs=-1, verbose=1
        )
        
        grid_search.fit(X_train, y_train)
        
        print(f"Best Logistic Regression parameters: {grid_search.best_params_}")
        return grid_search.best_estimator_, grid_search.best_params_