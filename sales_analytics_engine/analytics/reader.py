"""Read CSV lazily."""

import csv
from typing import Generator

# file_path = r"C:\Users\amolb\Desktop\Python\python_projects\sales_analytics_engine\data\orders.csv"

def read_orders(file_path: str) -> Generator[dict[str, str], None, None]:
    """
    Read orders from a CSV file lazily.

    Args:
        file_path: Path to the orders CSV.

    Yields:
        One row at a time as a dictionary.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as csv_file:
        
            reader = csv.DictReader(csv_file)

            for row in reader:
                yield row
    
    except FileNotFoundError:
        print("File not found!")



if __name__ == "__main__":
    file_path = "data/orders.csv"

    for row in read_orders(file_path):
        print(row)
    orders = read_orders(file_path)

    print(type(orders))
    print(next(orders))
    print(next(orders))