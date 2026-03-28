import load_data
import db_ingestion
import clean_text

if __name__ == "__main__":
    load_data.main()
    clean_text.main()
    db_ingestion.main()