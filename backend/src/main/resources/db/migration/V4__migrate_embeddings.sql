INSERT INTO documentEmbedding(document_id, embedding)
SELECT
    id,
    embedding
FROM document
WHERE embedding IS NOT NULL;