from sqlalchemy import create_engine
import yaml
import os


def load_config():
    """
    Load configuration file.
    Uses config_docker.yaml when running inside Airflow/Docker.
    """

    project_root = os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )

    if os.getenv("AIRFLOW_HOME"):
        config_file = "config_docker.yaml"
    else:
        config_file = "config.yaml"

    with open(
        os.path.join(project_root, config_file),
        "r"
    ) as f:
        return yaml.safe_load(f)


def get_engine():
    """
    Create and return SQLAlchemy engine.
    """

    config = load_config()

    db = config["database"]

    database_url = (
        f"postgresql://{db['user']}:{db['password']}"
        f"@{db['host']}:{db['port']}/{db['dbname']}"
    )

    return create_engine(database_url)


# Optional global engine
engine = get_engine()