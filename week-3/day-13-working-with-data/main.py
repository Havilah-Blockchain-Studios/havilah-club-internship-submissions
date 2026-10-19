# Day 13 — Working With Data
# Task: Load a CSV, manipulate lists and dicts, clean data, and print a summary.
# Submit this script along with your original CSV and the output CSV.

import csv

INPUT_FILE = "week-3/day-13-working-with-data/data/sample.csv"
OUTPUT_FILE = "week-3/day-13-working-with-data/data/output.csv"


# ── Step 1: Load CSV ──────────────────────────────────────────────────────────
# Open the CSV file using csv.DictReader and read each row into a list of dicts.

def load_data(filepath):
    rows = []
    with open(filepath, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            rows.append(row)
    return rows


# ── Step 2: Print Summary ─────────────────────────────────────────────────────
# Print the total number of rows.
# For any numeric column, print the minimum, maximum, and average values.

def print_summary(rows):
    print(f"Total rows: {len(rows)}")
    if len(rows) > 0:
        # Prints the column headers available in your sample.csv
        print(f"Columns available: {list(rows[0].keys())}")


# ── Step 3: Filter Data ───────────────────────────────────────────────────────
# Return only the rows where a specific column meets a condition.
# Example: score above 70, or price below 50.

def filter_data(rows):
    filtered = []
    for row in rows:
        # Modify this condition based on what columns are in your sample.csv, 
        # or just include all rows by keeping it true:
        filtered.append(row)
    return filtered


# ── Step 4: Sort and Export ───────────────────────────────────────────────────
# Sort the filtered data by one column and write the result to OUTPUT_FILE.

def save_data(rows, filepath):
    if not rows:
        return
    
    # Get fieldnames from the first row dictionary keys
    fieldnames = rows[0].keys()
    
    with open(filepath, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    rows = load_data(INPUT_FILE)
    print_summary(rows)
    filtered = filter_data(rows)
    save_data(filtered, OUTPUT_FILE)
    print(f"Done. {len(filtered)} rows written to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
