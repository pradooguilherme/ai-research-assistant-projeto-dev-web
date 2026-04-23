import pandas as pd
from db import connection

PATH = "ml/classification/data/classification_data.csv"

query = ("WITH valid_categories AS ("
         "  SELECT d.category"
         "  FROM document d"
         "  INNER JOIN document_embedding e"
         "      ON d.id = e.document_id"
         "  GROUP BY d.category "
         "  HAVING COUNT(*) >= 500"
         ") "
         "SELECT category, embedding "
         "FROM ("
         "      SELECT d.category,"
         "             e.embedding,"
         "             ROW_NUMBER() OVER ("
         "                  PARTITION BY d.category "
         "                  ORDER BY RANDOM()"
         ") AS rn "
         "FROM document d "
         "INNER JOIN document_embedding e "
         "  ON d.id = e.document_id "
         "INNER JOIN valid_categories vc "
         "  ON d.category = vc.category "
         ") t "
         "WHERE rn <= 500;")

conn = connection.connect_to_database()
df = pd.read_sql_query(query, conn)
df.to_csv(PATH, index=False)