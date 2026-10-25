# Day 15 — Python Automation Project
# Choose one project type and implement it here:
#
#   A) File Organiser  — scans a folder and moves files into subfolders by extension
#   B) Report Generator — reads a CSV and produces a formatted text summary
#   C) Data Cleaner    — removes duplicate rows, strips whitespace, standardises columns
#
# Submit the complete project (this file + data folder + README.md) to GitHub.

import os
import csv
# import shutil   # uncomment if using File Organiser
# import csv      # uncomment if using Report Generator or Data Cleaner


# ── Configuration ─────────────────────────────────────────────────────────────
# Set your input/output paths here so they are easy to find and change.

INPUT_PATH = "data/"
OUTPUT_PATH = "data/output/"


# ── Core Functions ─────────────────────────────────────────────────────────────
# Break your project into small, clearly named functions.
# Each function should do one thing.

def clean_value(value):

    """Remove leading and trailing whitespace from a value."""

    return value.strip() if value else ""

def clean_row(row):

    """Clean whitespace from every value in a row."""

    return [clean_value(value) for value in row]

def process(input_path, output_path):

    """Clean a CSV file and save the cleaned data."""

    # Find CSV files in the input directory, excluding the output directory.

    os.makedirs(output_path, exist_ok=True)

    csv_files = [

        file for file in os.listdir(input_path)

        if file.lower().endswith(".csv")

        and os.path.isfile(os.path.join(input_path, file))

    ]

    if not csv_files:

        print("No CSV files found in the input folder.")

        return

    for filename in csv_files:

        source_file = os.path.join(input_path, filename)

        output_file = os.path.join(

            output_path, f"cleaned_{filename}"

        )

        try:

            with open(source_file, "r", newline="", encoding="utf-8-sig") as file:

                reader = csv.reader(file)

                rows = list(reader)

            if not rows:

                print(f"Skipped empty file: {filename}")

                continue

            # Clean the header.

            header = clean_row(rows[0])

            # Remove completely empty rows.

            data_rows = [

                clean_row(row)

                for row in rows[1:]

                if any(value.strip() for value in row)

            ]

            # Remove duplicate rows while preserving their original order.

            unique_rows = []

            seen = set()

            for row in data_rows:

                row_key = tuple(row)

                if row_key not in seen:

                    seen.add(row_key)

                    unique_rows.append(row)

            # Save the cleaned CSV.

            with open(

                output_file, "w", newline="", encoding="utf-8"

            ) as file:

                writer = csv.writer(file)

                writer.writerow(header)

                writer.writerows(unique_rows)

            removed = len(data_rows) - len(unique_rows)

            print(f"\nProcessed: {filename}")

            print(f"Original data rows: {len(rows) - 1}")

            print(f"Cleaned data rows: {len(unique_rows)}")

            print(f"Duplicate rows removed: {removed}")

            print(f"Saved to: {output_file}")

        except (OSError, csv.Error, UnicodeError) as error:

            print(f"Error processing {filename}: {error}")


# ── Main ──────────────────────────────────────────────────────────────────────
def main():

    print("Starting Data Cleaner...")

    if not os.path.isdir(INPUT_PATH):

        print(f"Input directory not found: {INPUT_PATH}")

        return

    process(INPUT_PATH, OUTPUT_PATH)

    print("\nData cleaning complete.")

if __name__ == "__main__":

    main()
