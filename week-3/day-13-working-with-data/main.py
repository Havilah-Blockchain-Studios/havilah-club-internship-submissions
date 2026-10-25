# Day 13 — Working With Data

import csv
import os


# Find the folder where this main.py file is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

INPUT_FILE = os.path.join(BASE_DIR, "data", "sample.csv")
OUTPUT_FILE = os.path.join(BASE_DIR, "data", "processed.csv")


# Step 1: Load CSV
def load_data(file_path):
    rows = []

    with open(file_path, "r", newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)

        for row in reader:
            rows.append(row)

    return rows


# Step 2: Clean and convert data
def clean_data(rows):
    for row in rows:
        row["Name"] = row["Name"].strip().lower()
        row["Score"] = float(row["Score"].strip())

    return rows


# Step 3: Print Summary
def print_summary(rows):
    scores = [row["Score"] for row in rows]

    print("Total records:", len(rows))
    print("Minimum score:", min(scores))
    print("Maximum score:", max(scores))
    print("Average score:", sum(scores) / len(scores))


# Step 4: Filter Data
def filter_data(rows):
    filtered = []

    for row in rows:
        if row["Score"] >= 70:
            filtered.append(row)

    return filtered


# Step 5: Sort and Export
def save_data(rows, file_path):
    rows.sort(key=lambda row: row["Score"], reverse=True)

    with open(file_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)


# Main
def main():
    rows = load_data(INPUT_FILE)

    if not rows:
        print("No records found in the CSV file.")
        return

    rows = clean_data(rows)

    print_summary(rows)

    filtered = filter_data(rows)

    save_data(filtered, OUTPUT_FILE)

    print(f"Done. {len(filtered)} rows written to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
