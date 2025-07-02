import pandas as pd
import os

RAW_PATH = "data/raw/energy.csv"
PROCESSED_PATH = "data/processed/cleaned_energy.csv"

def preprocess():
    df = pd.read_csv(RAW_PATH, parse_dates=['Datetime'])
    
    # Set datetime index
    df = df.set_index("Datetime").sort_index()
    
    # Optional: Fill missing values
    df = df.fillna(method="ffill")

    # Save
    os.makedirs(os.path.dirname(PROCESSED_PATH), exist_ok=True)
    df.to_csv(PROCESSED_PATH)
    print(f"✅ Preprocessed data saved to: {PROCESSED_PATH}")

if __name__ == "__main__":
    preprocess()
