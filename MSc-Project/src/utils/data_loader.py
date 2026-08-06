"""
Data loading utilities for churn prediction project.
"""

import pandas as pd
import os
import warnings
warnings.filterwarnings('ignore')


class DataLoader:
    """Class for loading data from various sources."""
    
    def __init__(self, data_dir='data'):
        """
        Initialize the DataLoader.
        
        Args:
            data_dir: Directory containing data files
        """
        self.data_dir = data_dir
    
    def load_csv(self, filename, **kwargs):
        """
        Load data from CSV file.
        
        Args:
            filename: Name of the CSV file
            **kwargs: Additional arguments for pd.read_csv
            
        Returns:
            DataFrame with loaded data
        """
        file_path = os.path.join(self.data_dir, filename)
        
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
        
        data = pd.read_csv(file_path, **kwargs)
        print(f"Loaded {len(data)} rows from {filename}")
        
        return data
    
    def load_bank_data(self, filename='bank-full.csv'):
        """
        Load bank marketing data.
        
        Args:
            filename: Name of the bank data file
            
        Returns:
            DataFrame with bank marketing data
        """
        return self.load_csv(filename, sep=';')
    
    def load_telco_data(self, filename='telco.csv'):
        """
        Load telco customer churn data.
        
        Args:
            filename: Name of the telco data file
            
        Returns:
            DataFrame with telco customer churn data
        """
        return self.load_csv(filename)