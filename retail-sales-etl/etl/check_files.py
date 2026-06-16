import yaml
import os

def load_config():
    with open("/opt/airflow/config_docker.yaml", "r") as file:
        return yaml.safe_load(file)
    

def main():

    config = load_config()

    raw_data_path = config["paths"]["raw_data"]

    files = [
        f for f in os.listdir(raw_data_path)
        if f.endswith(".csv")
    ]

    print(f"Files available: {len(files)}")


if __name__ == "__main__":
    main()

## Visually represents file detection

