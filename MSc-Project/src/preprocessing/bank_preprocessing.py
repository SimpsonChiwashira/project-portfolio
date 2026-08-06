"""
Bank marketing data preprocessing module.
Matches the exact methodology from the original Bank-Notebook.ipynb
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import joblib
import warnings
warnings.filterwarnings('ignore')


class BankDataPreprocessor:
    """Class for preprocessing bank marketing data using the original notebook methodology."""
    
    def __init__(self):
        """Initialize the BankDataPreprocessor."""
        self.scaler = None
        self.feature_columns = None
    
    def load_data(self, file_path):
        """
        Load bank marketing data from CSV file.
        Uses the exact method from the original notebook: manual parsing with semicolon delimiter.
        
        Args:
            file_path: Path to the CSV file
            
        Returns:
            DataFrame with loaded data
        """
        # Read the CSV file and split by semicolons (exact method from notebook)
        data = []
        with open(file_path, 'r') as file:
            for line in file:
                split_line = line.strip().split(';')
                data.append(split_line)
        
        # Convert the data into a DataFrame
        df = pd.DataFrame(data)
        
        # Remove double quotes from data
        df = df.applymap(lambda x: x.replace('"', '') if isinstance(x, str) else x)
        
        # Converting the first row as column name and resetting the index
        df.columns = df.iloc[0]
        df = df[1:]
        df = df.reset_index(drop=True)
        
        print(f"Data loaded: {df.shape[0]} samples, {df.shape[1]} features")
        return df
    
    def clean_data(self, data):
        """
        Clean the bank marketing data.
        Converts specific columns to numeric types as per the original notebook.
        
        Args:
            data: Raw DataFrame
            
        Returns:
            Cleaned DataFrame
        """
        # Converting the Object types into numeric fields (integers)
        # Exact columns from notebook: age, day, duration, campaign, pdays, previous
        def change_int(df):
            col = ['age', 'day', 'duration', 'campaign', 'pdays', 'previous']
            for val in col:
                df[val] = pd.to_numeric(df[val], errors='coerce', downcast='integer')
        change_int(data)
        
        # balance is the only floating point - convert from object dtype to float
        data['balance'] = pd.to_numeric(data['balance'], errors='coerce', downcast='float')
        
        # Rename the churn prediction column to churn
        data.rename(columns={'y': 'churn'}, inplace=True)
        
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
        # One-hot encode specific columns (exact columns from notebook)
        # marital, contact, job, education, poutcome
        # Note: NOT using drop_first=True to match original notebook
        data = pd.get_dummies(data=data, columns=['marital', 'contact', 'job', 'education', 'poutcome'])
        
        # Converting all the yes and no to a one or zero
        # Exact columns from notebook: default, housing, loan, churn
        def convert_cat(df):
            cols = ['default', 'housing', 'loan', 'churn']
            for col in cols:
                df[col].replace({'yes': 1, 'no': 0}, inplace=True)
        convert_cat(data)
        
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
            # age, balance, duration, pdays, previous, day, campaign
            scale_cols = ['age', 'balance', 'duration', 'pdays', 'previous', 'day', 'campaign']
            self.scaler = MinMaxScaler()
            data[scale_cols] = self.scaler.fit_transform(data[scale_cols])
        else:
            # Transform only
            scale_cols = ['age', 'balance', 'duration', 'pdays', 'previous', 'day', 'campaign']
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
        
        # Clean data (convert types and rename column)
        data = self.clean_data(data)
        
        # Encode categorical variables (one-hot encoding and binary conversion)
        data = self.encode_categorical(data)
        
        # Scale numerical features
        data = self.scale_features(data)
        
        # Separate features and target
        if 'churn' in data.columns:
            y = data['churn']
            X = data.drop('churn', axis=1)
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