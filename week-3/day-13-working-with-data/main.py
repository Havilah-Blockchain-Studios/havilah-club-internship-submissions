# Day 13 — Working With Data
# Task: Load a CSV, manipulate lists and dicts, clean data, and print a summary.
# Submit this script along with your original CSV and the output CSV.

import csv

INPUT_FILE = "week-3/day-13-working-with-data/data/game_store.csv"
OUTPUT_FILE = "week-3/day-13-working-with-data/data/game_store_filtered.csv"


# ── Step 1: Load CSV ──────────────────────────────────────────────────────────
# Open the CSV file using csv.DictReader and read each row into a list of dicts.

def load_data(filepath):
    rows = []
    with open(filepath, "r", newline="") as groot:
        reader = csv.DictReader(groot)
        for row in reader:
            row["title"] = row["title"].strip()
            row["category"] = row["category"].strip()
            row["price"] = float(row["price"])
            row["quantity"] = int(row["quantity"])
            rows.append(row)
    return rows


# ── Step 2: Print Summary ─────────────────────────────────────────────────────
# Print the total number of rows.
# For any numeric column, print the minimum, maximum, and average values.

def print_summary(rows):
    prices = []
    for row in rows:
        prices.append(row["price"])

    print("Total records:", len(rows))
    print("Minimum price:", min(prices))
    print("Maximum price:", max(prices))
    print("Average price:", sum(prices) / len(prices))


# ── Step 3: Filter Data ───────────────────────────────────────────────────────
# Return only the rows where a specific column meets a condition.
# Example: score above 70, or price below 50.

def filter_data(rows):
    filtered = []
    for row in rows:
        if row["category"] == "Action RPG":
            filtered.append(row)
    return filtered


# ── Step 4: Sort and Export ───────────────────────────────────────────────────
# Sort the filtered data by one column and write the result to OUTPUT_FILE.

def save_data(rows, filepath):
    rows.sort(key= lambda x: x["price"], reverse=True)
    with open(filepath, "w", newline="") as groot:
        fieldnames = ["title", "category", "price", "quantity"]
        writer = csv.DictWriter(groot, fieldnames=fieldnames)
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
