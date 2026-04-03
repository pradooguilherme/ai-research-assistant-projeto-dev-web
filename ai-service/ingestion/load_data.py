import pandas as pd

RAW_DATASET_PATH = "../data/raw/arXiv_scientific_dataset.csv"
PREPROCESSED_PATH = "../data/raw/arXiv_scientific_dataset_loaded.csv"
CLEANED_DATASET_PATH = "../data/processed/cleaned_documents.csv"


def load_raw_data() -> pd.DataFrame:
    df = pd.read_csv(RAW_DATASET_PATH)
    print(f"Dataset loaded from {RAW_DATASET_PATH}, shape {df.shape}")
    return df

def load_processed_data() -> pd.DataFrame:
    df = pd.read_csv(PREPROCESSED_PATH)
    print(f"Dataset loaded from {PREPROCESSED_PATH}, shape {df.shape}")
    return df

def load_cleaned_data() -> pd.DataFrame:
    df = pd.read_csv(CLEANED_DATASET_PATH)
    print(f"Dataset loaded from {CLEANED_DATASET_PATH}, shape {df.shape}")
    return df

def show_data(df: pd.DataFrame):
    print(f"Dataset shape: {df.shape}")
    print("--------------")
    print(f"Columns: {df.columns}")
    print("--------------")
    print(f"Dataset null values: {df.isna().sum()}")
    print("--------------")
    print(f"Dataset unique values: {df.nunique().sort_values(ascending=False)}")
    print("--------------")
    print(f"Dataset data examples:")
    print(df.head())

def drop_duplicates(df: pd.DataFrame):
    df.drop_duplicates(inplace=True)
    df.drop_duplicates(subset=["summary", "title"], inplace=True)
    df.drop_duplicates(subset=["summary"], inplace=True)
    df.reset_index(drop=True, inplace=True)

def save_data(df: pd.DataFrame, path: str):
    df.to_csv(path, index=False)
    print(f"Dataset saved to {path}")

def main():
    df = load_raw_data()
    drop_duplicates(df)
    show_data(df)
    save_data(df, PREPROCESSED_PATH)