from db.queries import run_query
from sentence_transformers import SentenceTransformer

def generate_embeddings(batch_size=100):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    select_query = ("""
    SELECT d.id, d.text_no_stopwords 
    FROM document d
    LEFT JOIN document_embedding de 
        ON d.id = de.document_id
    WHERE de.document_id IS NULL 
    LIMIT %s
    """) % batch_size

    insert_query = """
    INSERT INTO document_embedding (document_id, embedding) 
    VALUES (%s, %s) 
    """

    while True:
        df = run_query(select_query)

        if df.empty:
            print("No documents found. Process finished.")
            break

        df.rename(columns={df.columns[0]: "id", df.columns[1]: "text_no_stopwords"}, inplace=True)

        embeddings = []
        for _, row in df.iterrows():
            embedding = model.encode(row["text_no_stopwords"]).tolist()
            embeddings.append([row["id"], embedding])

        for embedding in embeddings:
            run_query(insert_query, [embedding[0], embedding[1]])

        print(f"Loaded {len(embeddings)} embeddings")

if __name__ == "__main__":
    generate_embeddings()