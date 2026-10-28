# Day 15 - Python Automation Project
# Option B: Report Generator

import csv
import os

# --- Configuration ---
INPUT_PATH = "data/students.csv"
OUTPUT_PATH = "data/output/report.txt"


# --- Core Functions ---

def read_csv_scores(filepath: str) -> list[dict]:
    """Reads CSV file, validates required columns, and filters out invalid rows."""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found at: '{filepath}'")

    records = []
    with open(filepath, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        # Edge Case: Check for empty header or missing required fields
        if not reader.fieldnames or "name" not in reader.fieldnames or "score" not in reader.fieldnames:
            raise ValueError("Invalid CSV format: Must contain 'name' and 'score' headers.")

        for row_idx, row in enumerate(reader, start=2):
            name = row.get("name", "").strip() if row.get("name") else ""
            score_raw = row.get("score", "").strip() if row.get("score") else ""

            # Edge Case: Skip blank or empty fields
            if not name or not score_raw:
                continue

            # Edge Case: Skip non-numeric values
            try:
                score = float(score_raw)
                records.append({"name": name, "score": score})
            except ValueError:
                continue

    if not records:
        raise ValueError("No valid student score records found in CSV file.")

    return records


def calculate_metrics(records: list[dict]) -> dict:
    """Calculates total records, average score, highest score, and lowest score."""
    scores = [r["score"] for r in records]

    total_count = len(scores)
    avg_score = sum(scores) / total_count
    max_score = max(scores)
    min_score = min(scores)

    top_students = [r["name"] for r in records if r["score"] == max_score]
    bottom_students = [r["name"] for r in records if r["score"] == min_score]

    return {
        "count": total_count,
        "average": avg_score,
        "highest_score": max_score,
        "highest_performers": ", ".join(top_students),
        "lowest_score": min_score,
        "lowest_performers": ", ".join(bottom_students),
    }


def generate_report(metrics: dict, output_filepath: str) -> str:
    """Formats calculated metrics and saves the result to a text report."""
    report_text = (
        "========================================\n"
        "        STUDENT PERFORMANCE REPORT      \n"
        "========================================\n"
        f"Total Valid Records Analyzed : {metrics['count']}\n"
        f"Average Score                : {metrics['average']:.2f}\n"
        f"Highest Score                : {metrics['highest_score']} ({metrics['highest_performers']})\n"
        f"Lowest Score                 : {metrics['lowest_score']} ({metrics['lowest_performers']})\n"
        "========================================"
    )

    output_dir = os.path.dirname(output_filepath)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)

    with open(output_filepath, mode="w", encoding="utf-8") as f:
        f.write(report_text)

    return report_text


def process(input_path=INPUT_PATH, output_path=OUTPUT_PATH):
    """Executes the full pipeline required by the internship template."""
    try:
        records = read_csv_scores(input_path)
        metrics = calculate_metrics(records)
        report = generate_report(metrics, output_path)
        print(report)
        print(f"\nReport successfully generated at: {output_path}")
    except (FileNotFoundError, ValueError) as err:
        print(f"ERROR: {err}")


if __name__ == "__main__":
    process()