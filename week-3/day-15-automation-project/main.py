# Day 15 — Python Automation Project
# Choose one project type and implement it here:
#
#   A) File Organiser  — scans a folder and moves files into subfolders by extension
#   B) Report Generator — reads a CSV and produces a formatted text summary
#   C) Data Cleaner    — removes duplicate rows, strips whitespace, standardises columns
#
# Submit the complete project (this file + data folder + README.md) to GitHub.




# Working on Report Generator

# import shutil   # uncomment if using File Organiser

import os
import csv      # uncomment if using Report Generator or Data Cleaner


# ── Configuration ─────────────────────────────────────────────────────────────
# Set your input/output paths here so they are easy to find and change.

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_PATH = os.path.join(BASE_DIR, "data") + "/"
OUTPUT_PATH = os.path.join(BASE_DIR, "data", "output") + "/"
INPUT_FILE = "scores.csv"
OUTPUT_FILE = "report.txt"


# ── Core Functions ─────────────────────────────────────────────────────────────
# Break your project into small, clearly named functions.
# Each function should do one thing.

def read_records(csv_path):
    # TODO: implement your chosen project logic here
    
    pass

    records = []
    skipped = 0
    
    with open(csv_path, newline="") as file:
        reader = csv.DictReader(file)
        
        if reader.fieldnames is None:
            raise ValueError("The csv file is empty.")
        
        columns = [c.strip().lower() for c in reader.fieldnames]
        if "name" not in columns or "score" not in columns:
            raise ValueError("The csv must have 'name' and 'score' columns.")
        
        for row in reader:
            
            row = {k.strip().lower(): (v or"").strip()for k,v, in row.items() if k}
            name, score_text = row["name"], row["score"]
            
            if not name or not score_text:
                skipped += 1
                continue
            
            try:
                score = float(score_text)
            except ValueError:
                skipped += 1
                continue
            
            records.append((name, score))
            
    return records, skipped


def calculate_stats(records):
    
    scores = [score for _, score in records]
    return {
        "count": len(scores),
        "average": sum(scores) / len(scores),
        "highest": max(records, key=lambda r: r[1]),
        "lowest": min(records, key=lambda r: r[1])
    }
    
    
def format_report(stats, skipped):
    
    line = "=" * 36
    lines = [
        line,
        "          SCORE REPORT",
        line,
        f"Number of records : {stats['count']}"
        f"Average           : {stats['average']:.2f}"
        f"Highest score     : {stats['highest'][1]:g} ({stats['highest'][0]})"
        f"Lowest score      : {stats['lowest'][1]:g} ({stats['lowest'][0]})"
    ]
    if skipped:
        lines.append(f"Rows skipped     :{skipped} (blank or invalid)")
        lines.append(line)
    return "\n" .join(lines)
    
    
def save_report(text, report_path):
    os.makedirs(os.path.dirname(report_path), exist_ok=True)
    with open(report_path, "w")as file:
        file.write(text + "\n")
    
def process(input_path, output_path):
    
    csv_path = os.path.join(input_path, INPUT_FILE)
    report_path = os.path.join(output_path, OUTPUT_FILE)
    
    try:
        records, skipped = read_records(csv_path)
    except FileNotFoundError:
        print(f"Error: {csv_path}' was not found.Check the folder and file name.")
        return
    except ValueError as error:
        print (f"Error: {error}")
        return
    
    if not records:
        print("Error: no valid records found, so no report was created.")
        return
    stats = calculate_stats(records)
    report = format_report(stats, skipped)
    print(report)
    save_report(report, report_path)
    print(f"report saved to {report_path}")


# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    print("Starting automation...")
    process(INPUT_PATH, OUTPUT_PATH)
    print("Done.")


if __name__ == "__main__":
    main()
