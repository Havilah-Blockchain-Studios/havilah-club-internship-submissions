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

INPUT_FILE = "week-3/day-15-automation-project/data/scores.csv"
OUTPUT_FILE = "week-3/day-15-automation-project/data/output/report.txt"


# ── Core Functions ─────────────────────────────────────────────────────────────
# Break your project into small, clearly named functions.
# Each function should do one thing.

def read_scores_from_csv(file_path):
    """
    Function 1: Reads data from a CSV file.
    Extracts the names and numeric scores into a list of dictionaries.
    """
    records = []
    
    # Check if the input file actually exists before trying to open it
    if not os.path.exists(file_path):
        print(f"[Error] The input file '{file_path}' does not exist.")
        return None

    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Strip whitespace and convert the score string to an integer
            name = row['name'].strip()
            score = int(row['score'].strip())
            records.append({"name": name, "score": score})
            
    return records

def calculate_statistics(records):
    """
    Function 2: Performs mathematical aggregations on the scores dataset.
    Calculates total records, average score, highest score, and lowest score.
    """
    if not records:
        return None

    # Isolate all score integers into a single list for easy mathematical calculations
    scores = [r["score"] for r in records]
    
    total_records = len(scores)
    highest_score = max(scores)
    lowest_score = min(scores)
    average_score = sum(scores) / total_records

    # Find the student names matching the max and min scores for a richer report
    highest_scorer = next(r["name"] for r in records if r["score"] == highest_score)
    lowest_scorer = next(r["name"] for r in records if r["score"] == lowest_score)

    # Pack metrics into a dictionary mapping payload
    stats = {
        "total": total_records,
        "average": round(average_score, 2),
        "highest_val": highest_score,
        "highest_name": highest_scorer,
        "lowest_val": lowest_score,
        "lowest_name": lowest_scorer
    }
    return stats


def generate_formatted_report(stats, output_path):
    """
    Function 3: Generates a formatted multi-line string text report
    and writes it directly to the designated output folder path.
    """
    # Ensure the target nested directory structure exists before writing a file
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    report_content = f"""==================================================
        STUDENT PERFORMANCE AUTOMATED REPORT          
==================================================
Total Records Processed : {stats['total']}
Average Class Score     : {stats['average']}
--------------------------------------------------
Highest Score Achieved  : {stats['highest_val']} ({stats['highest_name']})
Lowest Score Achieved   : {stats['lowest_val']} ({stats['lowest_name']})
==================================================
Report generated automatically by Day 15 Engine.
"""

    # Write the string report block out to disk
    with open(output_path, mode='w', encoding='utf-8') as file:
        file.write(report_content)

    # Also display it live on the terminal engine interface
    print(report_content)


def process(input_path, output_path):
    """
    The orchestrator function tied directly to your template's process block.
    """
    print(f"Reading input data from: {input_path}...")
    data_records = read_scores_from_csv(input_path)
    
    if data_records:
        print(f"Analyzing data and aggregating metrics...")
        computed_stats = calculate_statistics(data_records)
        
        print(f"Writing final summary out to: {output_path}...\n")
        generate_formatted_report(computed_stats, output_path)


# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    print("Starting automation...")
    process(INPUT_FILE, OUTPUT_FILE)
    print("Done.")


if __name__ == "__main__":
    main()
