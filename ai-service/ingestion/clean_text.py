from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
import re
import pandas as pd

PATH_TO_DATASET = "../data/raw/arXiv_scientific_dataset_loaded.csv"
PROCESSED_PATH = "../data/processed/cleaned_documents.csv"

def load_data() -> pd.DataFrame:
    return pd.read_csv(PATH_TO_DATASET)

def save_clean_text(df: pd.DataFrame):
    df.to_csv(PROCESSED_PATH, index=False)
    print(f"Dataset cleaned saved to {PROCESSED_PATH}")

def clean_text(text: str) -> str:
    if not isinstance(text, str):
        return ""

    # Remove URLs
    text = re.sub(r"http\S+", "", text)
    # Remove special characters
    text = re.sub(r"[^a-zA-Z0-9\s]", " ", text)
    # Remove extras spaces
    text = re.sub(r"\s+", " ", text)
    # Turn text in lowercase
    text = text.lower()

    return text.strip()

def remove_small_texts(df: pd.DataFrame) -> pd.DataFrame:
    df = df[df["summary_word_count"] > 50]
    return df

def remove_stopwords(text: str) -> str:
    words = text.split()
    filtered = [w for w in words if w not in ENGLISH_STOP_WORDS]
    return " ".join(filtered)

def main():
    df = load_data()
    df = remove_small_texts(df)
    df["summary"] = df["summary"].apply(clean_text)
    df.drop_duplicates(subset=["summary"], inplace=True)
    df["title"] = df["title"].apply(clean_text)
    df["text"] = "title: " + df["title"] + " abstract: " + df["summary"]
    df["text_no_stopwords"] = df["text"].apply(remove_stopwords)
    df.reset_index(drop=True, inplace=True)
    save_clean_text(df)