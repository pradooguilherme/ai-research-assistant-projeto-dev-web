CREATE TABLE documentEmbedding (
    id SERIAL PRIMARY KEY,
    document_id BIGINT REFERENCES document(id),
    embedding float8[]
);;