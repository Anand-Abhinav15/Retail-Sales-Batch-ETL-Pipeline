import pandas as pd
from db import get_engine

def get_processed_files():

    engine = get_engine()

    query = """
    SELECT file_name FROM processed_files
    """

    df = pd.read_sql(query, engine)

    return set(df["file_name"].tolist())


def mark_file_processed(file_name):
    
    engine = get_engine()

    query = f"""
    INSERT INTO processed_files(file_name)
    VALUES ('{file_name}')
    ON CONFLICT (file_name)
    DO NOTHING;
    """

    with engine.begin() as conn:
        conn.exec_driver_sql(query)


