import pandas as pd
import random
import os
from faker import Faker
from datetime import datetime, timedelta

#Initialize Faker
fake = Faker()

#Output directory for the generated CSV files
OUTPUT_DIR = "data/raw_csv"
os.makedirs(OUTPUT_DIR, exist_ok=True)

#Static values
payment_methods = [
    "Credit Card",
    "Debit Card",
    "UPI",
    "Cash",
    "Net Banking"
]

regions = [
    "North",
    "South",
    "East",
    "West"
]

# Date Configuration
start_date = datetime(2026, 1, 1)
num_days = 5
rows_per_day = 500

# Generate files
for day in range(num_days):
    current_date = start_date + timedelta(days=day)
    records = []

    for i in range(rows_per_day):
        record = {
            "order_id": f"ORD_{day+1}_{i+1}",
            "customer_id": random.randint(1000, 9999),
            "product_id": random.randint(100, 999),
            "store_id": random.randint(1, 20),
            "order_date": current_date.strftime("%Y-%m-%d"),
            "quantity": random.randint(1, 10),
            "unit_price": round(random.uniform(10.0, 500.0), 2),
            "payment_method": random.choice(payment_methods),
            "region": random.choice(regions)
        }
        records.append(record)

    # Convert to DataFrame
    df = pd.DataFrame(records)

    # Create Filename
    file_name = f"sales_{current_date.strftime('%Y_%m_%d')}.csv"
    file_path = os.path.join(OUTPUT_DIR, file_name)

    # Save to CSV
    df.to_csv(file_path, index = False)

    print(f"Generated: {file_name} ({len(df)} rows)")

print("\nAll sales files generated successfully!")


