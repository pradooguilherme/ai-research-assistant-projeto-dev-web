from db.queries import run_query
from sentence_transformers import SentenceTransformer

def generate_embeddings(batch_size=100):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    select_query = "SELECT id, text_no_stopwords FROM document WHERE embedding IS NULL LIMIT %s" % batch_size
    update_query = "UPDATE document SET embedding = %s WHERE id = %s"

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
            run_query(update_query, [embedding[1], embedding[0]])

        print(f"Loaded {len(embeddings)} embeddings")

if __name__ == "__main__":
    generate_embeddings()