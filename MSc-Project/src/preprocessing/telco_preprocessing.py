"""
Telco customer churn data preprocessing module.
Matches the exact methodology from the original Telco-Notebook.ipynb
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import joblib
import warnings
warnings.filterwarnings('ignore')


class TelcoDataPreprocessor:
    """Class for preprocessing telco customer churn data using the original notebook methodology."""
    
    def __init__(self):
        """Initialize the TelcoDataPreprocessor."""
        self.scaler = None
        self.feature_columns = None
    
    def load_data(self, file_path):
        """
        Load telco customer churn data from CSV file.
        Uses the exact method from the original notebook: manual parsing with comma delimiter.
        
        Args:
            file_path: Path to the CSV file
            
        Returns:
            DataFrame with loaded data
        """
        # Read the CSV file and split by commas (exact method from notebook)
        data = []
        with open(file_path, 'r') as file:
            for line in file:
                split_line = line.strip().split(',')
                data.append(split_line)
        
        # Convert the data into a DataFrame
        df = pd.DataFrame(data)
        
        # Removing the strings on column names and anything which has a double quote
        df = df.applymap(lambda x: x.replace('"', '') if isinstance(x, str) else x)
        
        # Converting the first row as column name and resetting the index
        df.columns = df.iloc[0]
        df = df[1:]
        df = df.reset_index(drop=True)
        
        print(f"Data loaded: {df.shape[0]} samples, {df.shape[1]} features")
        return df
    
    def clean_data(self, data):
        """
        Clean the telco customer churn data.
        Converts specific columns to numeric types and handles missing values as per the original notebook.
        
        Args:
            data: Raw DataFrame
            
        Returns:
            Cleaned DataFrame
        """
        # Convert MonthlyCharges and TotalCharges to numeric
        data['MonthlyCharges'] = pd.to_numeric(data['MonthlyCharges'], errors='coerce')
        data['TotalCharges'] = pd.to_numeric(data['TotalCharges'], errors='coerce')
        
        # Drop the first column (customerID) - exact method from notebook
        data = data.drop(data.columns[0], axis=1)
        
        return data
    
    def encode_categorical(self, data):
        """
        Encode categorical variables.
        Uses the exact encoding method from the original notebook.
        
        Args:
            data: DataFrame with categorical variables
            
        Returns:
            DataFrame with encoded variables
        """
        # Replace specific values to reduce categories (exact method from notebook)
        # Replace 'No internet service' and 'No phone service' with 'No'
        data.replace('No internet service', 'No', inplace=True)
        data.replace('No phone service', 'No', inplace=True)
        
        # Encode gender: Female=1, Male=0
        data['gender'].replace({'Female': 1, 'Male': 0}, inplace=True)
        
        # Converting all the yes and no to a one or zero
        # Exact columns from notebook
        def convert_cat(df):
            cols = ['Partner', 'Dependents', 'PhoneService', 'MultipleLines', 'OnlineSecurity',
                    'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV',
                    'StreamingMovies', 'PaperlessBilling', 'Churn']
            for col in cols:
                df[col].replace({'Yes': 1, 'No': 0}, inplace=True)
        convert_cat(data)
        
        # One-hot encode specific columns (exact columns from notebook)
        # InternetService, Contract, PaymentMethod
        # Note: NOT using drop_first=True to match original notebook
        data = pd.get_dummies(data=data, columns=['InternetService', 'Contract', 'PaymentMethod'])
        
        return data
    
    def scale_features(self, data):
        """
        Scale numerical features using MinMaxScaler.
        Uses the exact scaling method from the original notebook.
        
        Args:
            data: DataFrame with numerical features
            
        Returns:
            DataFrame with scaled features
        """
        if self.scaler is None:
            # Scale specific columns (exact columns from notebook)
            # MonthlyCharges, TotalCharges, tenure
            scale_cols = ['MonthlyCharges', 'TotalCharges', 'tenure']
            self.scaler = MinMaxScaler()
            data[scale_cols] = self.scaler.fit_transform(data[scale_cols])
        else:
            # Transform only
            scale_cols = ['MonthlyCharges', 'TotalCharges', 'tenure']
            data[scale_cols] = self.scaler.transform(data[scale_cols])
        
        return data
    
    def preprocess_pipeline(self, file_path):
        """
        Complete preprocessing pipeline.
        Follows the exact sequence from the original notebook.
        
        Args:
            file_path: Path to the raw data file
            
        Returns:
            Preprocessed DataFrame with features and target
        """
        # Load data
        data = self.load_data(file_path)
        
        # Clean data (convert types and drop customerID)
        data = self.clean_data(data)
        
        # Encode categorical variables (replace values, binary conversion, one-hot encoding)
        data = self.encode_categorical(data)
        
        # Scale numerical features
        data = self.scale_features(data)
        
        # Separate features and target
        if 'Churn' in data.columns:
            y = data['Churn']
            X = data.drop('Churn', axis=1)
        else:
            X = data
            y = None
        
        # Store feature columns
        self.feature_columns = X.columns.tolist()
        
        if y is not None:
            return X, y
        return X
    
    def save_preprocessor(self, file_path):
        """
        Save the scaler to disk.
        
        Args:
            file_path: Path to save the scaler
        """
        joblib.dump(self.scaler, file_path)
        print(f"Scaler saved to: {file_path}")
    
    def load_preprocessor(self, file_path):
        """
        Load the scaler from disk.
        
        Args:
            file_path: Path to load the scaler from
        """
        self.scaler = joblib.load(file_path)
        print(f"Scaler loaded from: {file_path}")