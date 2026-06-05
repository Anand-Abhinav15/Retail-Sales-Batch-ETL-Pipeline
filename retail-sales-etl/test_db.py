from etl.db import get_engine

engine = get_engine()

with engine.connect() as conn:
    print("Database connection successful!")