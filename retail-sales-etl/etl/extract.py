import os
import pandas as pd
import yaml

def load_config():
    """
    Load configuration from config.yaml
    """
    with open("config.yaml", "r") as file:
        return yaml.safe_load(file)

def get_all_files(raw_data_path):
    """
    Get all CSV files from raw data folder
    """

    files = [
        file
        for file in os.listdir(raw_data_path)
        if file.endswith(".csv")
    ]

    return sorted(files)



def get_processed_files(tracking_file):
    """
    Read already processed files
    """

    if not os.path.exists(tracking_file):
        return set()
    
    with open(tracking_file, "r") as file:
        processed = {
            line.strip()
            for line in file.readlines()
            if line.strip()
        }
    
    return processed

def get_new_files(all_files, processed_files):
        """
        Compare all files vs processed files
        """

        return [
             file
             for file in all_files
             if file not in processed_files
        ]

def read_csv_file(file_path):
     """
     Read a CSV into DataFrame
     """

     df = pd.read_csv(file_path)

     return df

def mark_file_as_processed(file_name, tracking_file):
    """
    Save file name into tracking file
    """

    with open(tracking_file, "a") as file:
        file.write(file_name + "\n")

def main():
    config = load_config()
     
    raw_data_path = config["paths"]["raw_data"]
    tracking_file = config["paths"]["processed_tracking"]

    print("\n============ EXTRACT LAYER ============\n")

    all_files = get_all_files(raw_data_path)

    print(f"Total files found: {len(all_files)}")

    processed_files = get_processed_files(tracking_file)

    print(f"Already processed: {len(processed_files)}")

    new_files = get_new_files(
        all_files,
        processed_files
    )

    print(f"New files detected: {len(new_files)}")

    if not new_files:
        print("No new files to process.")
        return
    
    for file_name in new_files:
        print(f"Processing: {file_name}")

        file_path = os.path.join(
            raw_data_path,
            file_name
        )

        df = read_csv_file(file_path)

        print(f"Rows loaded: {len(df)}")

        print(df.head())

        # Temmporary:
        # later Airflow will call validation
        # validation(df)

        mark_file_as_processed(
            file_name, 
            tracking_file
        )

        print(f"{file_name} marked as processed.\n")

if __name__ == "__main__":
    main()



