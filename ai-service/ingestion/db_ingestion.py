import ast

import pandas as pd
import psycopg2

PATH_TO_DATASET = "../data/processed/cleaned_documents.csv"

def load_data(path: str) -> pd.DataFrame:
    return pd.read_csv(path)

def connect_to_database() -> psycopg2.extensions.connection:
    return psycopg2.connect(database="ai_research_assistant_db",
                            user="pradooguilherme",
                            password="gp2025@",
                            host="localhost")

def run_query(query: str, values=None):
    connection = connect_to_database()
    cursor = connection.cursor()

    try:
        if values is not None:
            cursor.execute(query, values)
        else:
            cursor.execute(query)

        if query.strip().lower().startswith("select"):
            result = cursor.fetchall()
            return pd.DataFrame(result)
        else:
            connection.commit()
            return None
    finally:
        cursor.close()
        connection.close()

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

                cursor.execute(query, values)

            except Exception as e:
                print("\nERRO NA INSERÇÃO")
                print(f"Linha do DataFrame: {i}")
                print("Valores:", data.to_string())
                print("Erro:", e)
                print("-" * 50)
                connection.rollback()  # evita travar a transação
                break  # para na primeira falha (melhor pra debug)

        connection.commit()

    finally:
        cursor.close()
        connection.close()

if __name__ == "__main__":
    df = load_data(PATH_TO_DATASET)
    db_ingestion(df)