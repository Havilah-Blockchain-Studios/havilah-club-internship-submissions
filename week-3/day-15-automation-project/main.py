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

INPUT_PATH = "week-3/day-15-automation-project/data/input.csv"
OUTPUT_PATH = "week-3/day-15-automation-project/data/output/cleaned_data.csv"


# ── Core Functions ─────────────────────────────────────────────────────────────
# Break your project into small, clearly named functions.
# Each function should do one thing.

def process(input_path, output_path):
    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    cleaned_rows = []
    seen = set()
    
    # Read the input CSV file
    with open(input_path, mode="r", encoding="utf-8") as infile:
        reader = csv.reader(infile)
        header = next(reader)
        # Standardise header: strip whitespace and lowercase
        cleaned_header = [h.strip().lower() for h in header]
        cleaned_rows.append(cleaned_header)
        
        for row in reader:
            # Strip whitespace from each field in the row
            cleaned_row = [cell.strip() for cell in row]
            
            # Convert row to a tuple to check for duplicates
            row_tuple = tuple(cleaned_row)
            if row_tuple not in seen and any(cleaned_row): # skip empty rows
                seen.add(row_tuple)
                cleaned_rows.append(cleaned_row)
                
    # Write the cleaned data to the output CSV file
    with open(output_path, mode="w", encoding="utf-8", newline="") as outfile:
        writer = csv.writer(outfile)
        writer.writerows(cleaned_rows)
        
    print(f"Data cleaned successfully! Saved to {output_path}")


# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    print("Starting automation...")
    process(INPUT_PATH, OUTPUT_PATH)
    print("Done.")


if __name__ == "__main__":
    main()
