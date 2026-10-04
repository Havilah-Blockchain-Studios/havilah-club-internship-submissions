# Day 13 — Working With Data
# Task: Load a CSV, manipulate lists and dicts, clean data, and print a summary.
# Submit this script along with your original CSV and the output CSV.

import csv

INPUT_FILE = "data/sample.csv"
OUTPUT_FILE = "data/output.csv"
FILTER_COLUMN = "score"
FILTER_THRESHOLD = 70

# ── Step 1: Load CSV ──────────────────────────────────────────────────────────
# Open the CSV file using csv.DictReader and read each row into a list of dicts.

def load_data(filepath):
    rows = []
    with open(filepath, mode="r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)
    return rows


# ── Step 2: Print Summary ─────────────────────────────────────────────────────
# Print the total number of rows.
# For any numeric column, print the minimum, maximum, and average values.

def print_summary(rows):
    print(f"Total rows: {len(rows)}")

    if not rows:
        return

    for column in rows[0].keys():
        values = []
        for row in rows:
            try:
                values.append(float(row[column]))
            except ValueError:
                pass

        if values:
            print(f"{column} -> min: {min(values)}, max: {max(values)}, average: {round(sum(values) / len(values), 2)}")

# ── Step 3: Filter Data ───────────────────────────────────────────────────────
# Return only the rows where a specific column meets a condition.
# Example: score above 70, or price below 50.

def filter_data(rows):
    filtered = []
    for row in rows:
        try:
            if float(row[FILTER_COLUMN]) > FILTER_THRESHOLD:
                filtered.append(row)
        except (ValueError, KeyError):
            continue
    return filtered

# ── Step 4: Sort and Export ───────────────────────────────────────────────────
# Sort the filtered data by one column and write the result to OUTPUT_FILE.

def save_data(rows, filepath):
    if not rows:
        return
    sorted_rows = sorted(rows, key=lambda row: float(row[FILTER_COLUMN]), reverse=True)
    with open(filepath, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(sorted_rows)


# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    rows = load_data(INPUT_FILE)
    print_summary(rows)
    filtered = filter_data(rows)
    save_data(filtered, OUTPUT_FILE)
    print(f"Done. {len(filtered)} rows written to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
