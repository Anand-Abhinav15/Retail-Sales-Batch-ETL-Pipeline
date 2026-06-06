import os
import pandas as pd
import yaml

from validations import run_validations
from transform import transform_data

from file_tracker import (
    get_processed_files,
    mark_file_processed
)


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
    Read CSV into dataframe
    """

    return pd.read_csv(file_path)


def main():

    config = load_config()

    raw_data_path = config["paths"]["raw_data"]

    print("\n============ EXTRACT LAYER ============\n")

    all_files = get_all_files(raw_data_path)

    print(f"Total files found: {len(all_files)}")

    # Read from PostgreSQL table
    processed_files = get_processed_files()

    print(f"Already processed: {len(processed_files)}")

    new_files = get_new_files(
        all_files,
        processed_files
    )

    print(f"New files detected: {len(new_files)}")

    if not new_files:
        print("\nNo new files to process.")
        return

    for file_name in new_files:

        print(f"\nProcessing: {file_name}")

        file_path = os.path.join(
            raw_data_path,
            file_name
        )

        # ====================================
        # EXTRACT
        # ====================================

        df = read_csv_file(file_path)

        print(f"Rows loaded: {len(df)}")

        # ====================================
        # VALIDATE
        # ====================================

        validation_results = run_validations(df)

        print(
            f"Validation Results: "
            f"{validation_results}"
        )

        # ====================================
        # TRANSFORM
        # ====================================

        df = transform_data(df)
        print(df.columns.tolist())

        print("\nTransformed Data:")

        print(
            f"\nRows after transformation: "
            f"{len(df)}"
        )

        print(df.head())

        # ====================================
        # MARK FILE PROCESSED
        # ====================================

        mark_file_processed(file_name)

        print(
            f"{file_name} marked as processed."
        )


if __name__ == "__main__":
    main()