import csv
import os
from tqdm import tqdm


def generate_csv(name: str = "data/soe_data.csv", data=None):
    if data is None or len(data) == 0:
        raise ValueError("Data should not be empty.")

    directory = os.path.dirname(name)
    os.makedirs(directory, exist_ok=True)
    with open(name, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        for row in tqdm(data, desc="Writing rows to CSV"):
            writer.writerow(row)
