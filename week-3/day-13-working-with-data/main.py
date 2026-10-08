# Day 13 — Working With Data
# Task: Load a CSV, manipulate lists and dicts, clean data, and print a summary.
# Submit this script along with your original CSV and the output CSV.

import csv

INPUT_FILE = "data/Student_Dataset.csv"
OUTPUT_FILE = "data/output.csv"


# ── Step 1: Load CSV ──────────────────────────────────────────────────────────
# Open the CSV file using csv.DictReader and read each row into a list of dicts.

def load_data(filepath):
    rows = []
    with open ("Student_Dataset.csv", "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            rows.append(row)
    return rows

# ---Step 2: clean and convert data --------------------------------------------

def clean_data(rows):
    for row in rows:
        row["Department"] = row["Department"].strip().title()
        row["Score"] = int(row["Score"].strip())
    return rows


# ── Step 3: Print Summary ─────────────────────────────────────────────────────
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
            print(f"{column} - min: {min(values)}, max: {max(values)}, average: {sum(values)/len(values):.2f}")
    pass


# ── Step 4: Filter Data ───────────────────────────────────────────────────────
# Return only the rows where a specific column meets a condition.
# Example: score above 70, or price below 50.

def filter_data(rows):
    filtered = []
    for row in rows:
        if row["Score"] > 65:
            filtered.append(row)
    return filtered


# ── Step 5: Sort and Export ───────────────────────────────────────────────────
# Sort the filtered data by one column and write the result to OUTPUT_FILE.

def save_data(rows, filepath):
    sorted_rows = sorted(rows, key=lambda row: row["Score"])
    with open(filepath, "w", newline="") as file:
        fieldnames = sorted_rows[0].keys()
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(sorted_rows)
    pass


# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    rows = load_data(INPUT_FILE)
    rows = clean_data(rows)
    print_summary(rows)
    filtered = filter_data(rows)
    print("LIST OF STUDENTS WITH SCORE ABOVE 65;")
    for row in filtered:
        print(row)
    save_data(filtered, OUTPUT_FILE)
    print(f"Done. {len(filtered)} rows written to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()