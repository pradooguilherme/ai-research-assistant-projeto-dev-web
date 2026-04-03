import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

def connect_to_database() -> psycopg2.extensions.connection:
    return psycopg2.connect(database=os.getenv("DB_NAME"),
                            user=os.getenv("DB_USER"),
                            password=os.getenv("DB_PASSWORD"),
                            host=os.getenv("DB_HOST", "localhost"))