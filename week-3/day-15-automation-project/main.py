# Day 15 — Python Automation Project
# Option B: Report Generator
# Reads a CSV of names and scores and writes a formatted text report.

import os
import csv


# ── Configuration ─────────────────────────────────────────────────────────────
INPUT_PATH = "data/scores.csv"
OUTPUT_PATH = "data/output/report.txt"


# ── Core Functions ─────────────────────────────────────────────────────────────
def read_scores(input_path):
    # Read the CSV and return a list of {"name": ..., "score": ...} dictionaries.
    # Returns None if the file can't be used.
    records = []
    try:
        with open(input_path, newline="", encoding="utf-8-sig") as file:
            reader = csv.DictReader(file)
            columns = reader.fieldnames
            
            # Edge case: empty file
            if not columns:
                print("Error: the CSV file is empty.")
                return None

            # Edge case: missing columns
            for needed in ("name", "score"):
                if needed not in columns:
                    print("Error: the CSV is missing the '" + needed + "' column.")
                    return None

            for row in reader:
                try:
                    records.append({"name": row["name"].strip(), "score": float(row["score"])})
                except (ValueError, TypeError, AttributeError):
                    # Edge case: blank or non-numeric score
                    print("Skipping row with a missing or invalid value:", row)
    except FileNotFoundError:
        # Edge case: missing input file
        print("Error: could not find '" + input_path + "'.")
        print("Check the file exists and run this script from the Day 15 folder.")
        return None
    return records

def calculate_stats(records):
    # Work out the count, average, highest and lowest scores
    total = 0
    highest = records[0]
    lowest = records[0]

    for record in records:
        total = total + record["score"]
        if record["score"] > highest["score"]:
            highest = record
        if record["score"] < lowest["score"]:
            lowest = record

    return {
        "count": len(records),
        "average": total / len(records),
        "highest": highest,
        "lowest": lowest,
    }


def build_report(stats):
    # Turn the numbers into a formatted block of text
    lines = [
        "=" * 30,
        "SCORE REPORT",
        "=" * 30,
        "Number of records: " + str(stats["count"]),
        "Average score: " + format(stats["average"], ".1f"),
        "Highest score: " + format(stats["highest"]["score"], ".1f")
        + " (" + stats["highest"]["name"] + ")",
        "Lowest score: " + format(stats["lowest"]["score"], ".1f")
        + " (" + stats["lowest"]["name"] + ")",
        "=" * 30,
    ]
    return "\n".join(lines)


def save_report(report, output_path):
    # Create the output folder if needed, then write the report to a file
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as file:
        file.write(report)


def process(input_path, output_path):
    # Input -> Process -> Output
    records = read_scores(input_path)
    if records is None:
        return

    # Edge case: no usable records
    if len(records) == 0:
        print("No valid records found, so there is nothing to report.")
        return

    stats = calculate_stats(records)
    report = build_report(stats)
    print(report)
    save_report(report, output_path)


# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    print("Starting automation...")
    process(INPUT_PATH, OUTPUT_PATH)
    print("Done.")


if __name__ == "__main__":
    main()