import yaml
from sqlalchemy import create_engine

def get_engine():

    with open("config.yaml", "r") as file:
        config = yaml.safe_load(file)

    db = config["database"]

    connection_string = (
        f"postgresql+psycopg2://"
        f"{db['user']}:{db['password']}"
        f"@{db['host']}: {db['port']}"
        f"/{db['dbname']}"
    )

    engine = create_engine(connection_string)

    return engine