from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
from ingestion.load_data import load_processed_data
from ingestion.load_data import save_data
import re
import pandas as pd

PROCESSED_PATH = "../data/processed/cleaned_documents.csv"

def clean_text(text: str) -> str:
    if not isinstance(text, str):
        return ""
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"[^a-zA-Z0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text)
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
    df = load_processed_data()
    df = remove_small_texts(df)
    df["summary"] = df["summary"].apply(clean_text)
    df.drop_duplicates(subset=["summary"], inplace=True)
    df["title"] = df["title"].apply(clean_text)
    df["text"] = "title: " + df["title"] + " abstract: " + df["summary"]
    df["text_no_stopwords"] = df["text"].apply(remove_stopwords)
    df.reset_index(drop=True, inplace=True)
    save_data(df, PROCESSED_PATH)