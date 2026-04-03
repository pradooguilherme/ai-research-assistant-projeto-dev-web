--ALTER TABLE document DROP COLUMN embedding;
SELECT count(*) FROM documentEmbedding;
SELECT count(*) FROM document WHERE embedding IS NOT NULL;