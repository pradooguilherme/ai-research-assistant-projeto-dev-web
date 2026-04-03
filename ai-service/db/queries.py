import pandas as pd
from db.connection import connect_to_database

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