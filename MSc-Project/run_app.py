"""
Run script for Streamlit applications.
Launches the churn prediction apps from the proper directory.
"""

import subprocess
import sys
import os

def main():
    # Get the project root directory
    project_root = os.path.dirname(os.path.abspath(__file__))
    
    # Change to the project root directory
    os.chdir(project_root)
    
    # Run the Streamlit app from the home page
    home_page = os.path.join(project_root, "deployment", "streamlit", "home.py")
    
    print(f"Starting Streamlit app from: {home_page}")
    print(f"Working directory: {os.getcwd()}")
    
    # Run streamlit
    subprocess.run([sys.executable, "-m", "streamlit", "run", home_page])

if __name__ == "__main__":
    main()