# Day 13 — Working With Data
# Task: Load a CSV, manipulate lists and dicts, clean data, and print a summary.
# Submit this script along with your original CSV and the output CSV.

import csv

INPUT_FILE = "data/sample.csv"
OUTPUT_FILE = "data/output.csv"


# ── Step 1: Load CSV ──────────────────────────────────────────────────────────
# Open the CSV file using csv.DictReader and read each row into a list of dicts.

def load_data(filepath):
    rows = []
    with open(filepath, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
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

    # Convert score values to numbers

    scores = []

    for row in rows:

        try:

            scores.append(float(row["score"]))

        except (ValueError, KeyError):

            continue

    if scores:

        minimum = min(scores)

        maximum = max(scores)

        average = sum(scores) / len(scores)

        print(f"Minimum score: {minimum}")

        print(f"Maximum score: {maximum}")

        print(f"Average score: {average:.2f}"
    
     


# ── Step 3: Filter Data ───────────────────────────────────────────────────────
# Return only the rows where a specific column meets a condition.
# Example: score above 70, or price below 50.

 def filter_data(rows):

    filtered = []

    for row in rows:

        try:

            if float(row["score"]) > 70:

                filtered.append(row)

        except (ValueError, KeyError):

            continue

    return filtered

# ── Step 4: Sort and Export ───────────────────────────────────────────────────
# Sort the filtered data by one column and write the result to OUTPUT_FILE.

    def save_data(rows, filepath):

    if not rows:

        print("No data to export.")

        return

    # Sort by score from highest to lowest

    rows = sorted(rows, key=lambda row: float(row["score"]), reverse=True)

    with open(filepath, "w", newline="", encoding="utf-8") as file:

        fieldnames = rows[0].keys()

        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()

        writer.writerows(rows
     
     


# ── Main ──────────────────────────────────────────────────────────────────────
     def main():

    rows = load_data(INPUT_FILE)

    print_summary(rows)

    filtered = filter_data(rows)

    save_data(filtered, OUTPUT_FILE)

    print(f"Done. {len(filtered)} rows written to {OUTPUT_FILE}")

if __name__ == "__main__":

    main()
