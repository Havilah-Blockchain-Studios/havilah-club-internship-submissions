# Day 15 — Python Automation Project
# Choose one project type and implement it here:
#
#   A) File Organiser  — scans a folder and moves files into subfolders by extension
#   B) Report Generator — reads a CSV and produces a formatted text summary
#   C) Data Cleaner    — removes duplicate rows, strips whitespace, standardises columns
#
# Submit the complete project (this file + data folder + README.md) to GitHub.

import os
# import shutil   # uncomment if using File Organiser
import csv      # uncomment if using Report Generator or Data Cleaner


# ── Configuration ─────────────────────────────────────────────────────────────
# Set your input/output paths here so they are easy to find and change.

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_FILE = os.path.join(BASE_DIR, "data", "scores.csv")
OUTPUT_FILE = os.path.join(BASE_DIR, "data", "output", "report.txt")

# ── Core Functions ─────────────────────────────────────────────────────────────
# Break your project into small, clearly named functions.
# Each function should do one thing.

def load_scores(filename):
    """Read the CSV and return a list of valid scores."""
    scores = []
    skipped = 0

    # Edge case 1: file does not exist
    try:
        with open(filename, newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            # Edge case 2: empty file or missing 'score' column
            if reader.fieldnames is None:
                print("Error: the file is empty.")
                return None
            if "score" not in reader.fieldnames:
                print("Error: the CSV has no 'score' column.")
                return None

            for row in reader:
                value = (row["score"] or "").strip()

                # Edge case 3: blank or non-number score -> skip the row
                try:
                    scores.append(float(value))
                except ValueError:
                    skipped += 1
    except FileNotFoundError:
        print(f"Error: {filename} was not found.")
        return None

    if skipped:
        print(f"Note: skipped {skipped} row(s) with a blank or invalid score.")
    return scores

def calculate_stats(scores):
    """Return count, average, highest and lowest score."""
    return {
        "count": len(scores),
        "average": sum(scores) / len(scores),
        "highest": max(scores),
        "lowest": min(scores),
    }


def build_report(stats):
    """Turn the stats into a formatted text report."""
    lines = [
        "=" * 30,
        "     SCORE REPORT",
        "=" * 30,
        f"Number of records : {stats['count']}",
        f"Average score     : {stats['average']:.2f}",
        f"Highest score     : {stats['highest']:.0f}",
        f"Lowest score      : {stats['lowest']:.0f}",
        "=" * 30,
    ]
    return "\n".join(lines)

def save_report(report, filename):
    """Save the report to a text file."""
    # Make the output folder if it doesn't exist yet
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w", encoding="utf-8") as file:
        file.write(report + "\n")

# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    print("Starting automation...")
    scores = load_scores(INPUT_FILE)

    # Stop if loading failed or there are no usable scores
    if scores is None:
        return
    if len(scores) == 0:
        print("Error: no valid scores found.")
        return

    stats = calculate_stats(scores)
    report = build_report(stats)
    print(report)
    save_report(report, OUTPUT_FILE)
    print(f"Report saved to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
