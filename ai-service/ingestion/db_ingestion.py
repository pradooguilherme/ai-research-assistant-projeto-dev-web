from db.connection import connect_to_database
from db.queries import run_query
from ingestion.load_data import load_cleaned_data
import ast
import pandas as pd

def db_ingestion(df: pd.DataFrame):
    query = """
    INSERT INTO document (
        authors,
        category,
        category_code,
        first_author,
        publication_date,
        summary,
        summary_word_count,
        text,
        text_no_stopwords,
        title,
        updated_date
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    connection = connect_to_database()
    cursor = connection.cursor()

    try:
        for i, data in df.iterrows():
            try:

                authors = ast.literal_eval(data["authors"]) if pd.notna(data["authors"]) else None

                values = (
                    authors,
                    data["category"],
                    data["category_code"],
                    data["first_author"],
                    pd.to_datetime(data["published_date"], errors="coerce").date()
                        if pd.notna(data["published_date"]) else None,
                    data["summary"],
                    int(data["summary_word_count"]) if pd.notna(data["summary_word_count"]) else None,
                    data["text"],
                    data["text_no_stopwords"],
                    data["title"],
                    pd.to_datetime(data["updated_date"], errors="coerce").date()
                        if pd.notna(data["updated_date"]) else None,
                )

                run_query(query, values)

            except Exception as e:
                print("\nERRO NA INSERÇÃO")
                print(f"Linha do DataFrame: {i}")
                print("Valores:", data.to_string())
                print("Erro:", e)
                print("-" * 50)
                connection.rollback()
                break

        connection.commit()

    finally:
        cursor.close()
        connection.close()

def main():
    df = load_cleaned_data()
    db_ingestion(df)