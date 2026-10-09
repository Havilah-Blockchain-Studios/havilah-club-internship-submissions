# Day 13 — Working With Data
# Task: Load a CSV, manipulate lists and dicts, clean data, and print a summary.
# Submit this script along with your original CSV and the output CSV.

import csv

INPUT_FILE = "data/sample.csv"
OUTPUT_FILE = "data/output.csv"


# ── Step 1: Load CSV ──────────────────────────────────────────────────────────
# Open the CSV file using csv.DictReader and read each row into a list of dicts.
# Also clean messy text and convert numeric fields to the right type.

def load_data(filepath):
    rows = []

    file = open(filepath, newline="")
    reader = csv.DictReader(file)

    for row in reader:
        # Remove extra spaces
        clean_name = row["name"].strip()

        # Replace symbols used instead of spaces
        clean_name = clean_name.replace("-", " ")
        clean_name = clean_name.replace("_", " ")
        clean_name = clean_name.replace("/", " ")

        # Fix inconsistent capitalization
        clean_name = clean_name.title()

        clean_category = row["category"].strip()
        clean_category = clean_category.lower()
        clean_category = clean_category.capitalize()

        # Convert numeric fields from string to number
        clean_price = float(row["price"].strip())
        clean_quantity = int(row["quantity"].strip())

        clean_row = {
            "name": clean_name,
            "price": clean_price,
            "quantity": clean_quantity,
            "category": clean_category,
        }

        rows.append(clean_row)

    file.close()
    return rows


# ── Step 2: Print Summary ─────────────────────────────────────────────────────
# Print the total number of rows.
# For any numeric column, print the minimum, maximum, and average values.

def print_summary(rows):
    total_records = len(rows)

    # Collect all prices into a separate list
    all_prices = []
    for row in rows:
        all_prices.append(row["price"])

    lowest_price = min(all_prices)
    highest_price = max(all_prices)
    total_price = sum(all_prices)
    average_price = total_price / total_records

    print("\n" + "=" * 40)
    print("           DATASET SUMMARY")
    print("=" * 40)
    print(f"Total Records : {total_records}")
    print(f"Minimum Price : {lowest_price:.2f}")
    print(f"Maximum Price : {highest_price:.2f}")
    print(f"Average Price : {average_price:.2f}")
    print("=" * 40)


# ── Step 3: Filter Data ───────────────────────────────────────────────────────
# Return only the rows where a specific column meets a condition.
# Example: score above 70, or price below 50.

def filter_data(rows):
    filtered = []

    for row in rows:
        if row["price"] < 50:
            filtered.append(row)

    return filtered


# ── Step 4: Sort and Export ───────────────────────────────────────────────────
# Sort the filtered data by one column and write the result to OUTPUT_FILE.

def save_data(rows, filepath):
    # Sort manually using sorted() with a plain function instead of a lambda
    def get_name(row):
        return row["name"]

    sorted_rows = sorted(rows, key=get_name)

    file = open(filepath, "w", newline="")
    fieldnames = ["name", "price", "quantity", "category"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    for row in sorted_rows:
        writer.writerow(row)

    file.close()


# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    rows = load_data(INPUT_FILE)
    print_summary(rows)
    filtered = filter_data(rows)
    save_data(filtered, OUTPUT_FILE)
    print(f"Done. {len(filtered)} rows written to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()