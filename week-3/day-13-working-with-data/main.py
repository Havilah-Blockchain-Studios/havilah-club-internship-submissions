# Day 13 — Working With Data
# Task: Load a CSV, manipulate lists and dicts, clean data, and print a summary.
# Submit this script along with your original CSV and the output CSV.

import csv

INPUT_FILE = "week-3/day-13-working-with-data/data/student_dataset.csv"
OUTPUT_FILE = "week-3/day-13-working-with-data/data/top_students_output.csv"

# — Step 1 & 2: Load CSV ————————————————————————————————————————————————
def load_data(filepath):
    rows = []
    try:
        with open(filepath, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Normalize all keys: strip whitespace and convert to lowercase
                normalized_row = {k.strip().lower(): v.strip() for k, v in row.items()}
                
                # Extract name and department safely
                cleaned_row = {
                    "name": normalized_row.get("name", normalized_row.get("student name", "")).strip().title(),
                    "department": normalized_row.get("department", "").strip().lower(),
                }
                
                # Look for score under common variations (score, scores, marks, grade, point)
                score_str = ""
                for key in ["score", "scores", "marks", "grade", "point"]:
                    if key in normalized_row:
                        score_str = normalized_row[key]
                        break
                
                # Convert score to float safely
                try:
                    cleaned_row["score"] = float(score_str)
                except ValueError:
                    cleaned_row["score"] = 0.0
                
                rows.append(cleaned_row)
        print(f"Successfully loaded and cleaned {len(rows)} records from {filepath}.")
    except FileNotFoundError:
        print(f"Error: The file {filepath} was not found.")
    return rows

# — Step 2 & 4: Print Summary & Analysis ——————————————————————————————
# Print total records and statistics (min, max, average) for numeric columns.
def print_summary(rows):
    if not rows:
        print("No data available for summary.")
        return

    print(f"\n--- DATASET ANALYSIS ---")
    print(f"Total Records: {len(rows)}")
    
    scores = [row["score"] for row in rows]
    
    if scores:
        print(f"Minimum Score: {min(scores)}")
        print(f"Maximum Score: {max(scores)}")
        print(f"Average Score: {sum(scores) / len(scores):.2f}")

# — Step 3 & 5: Filter Data —————————————————————————————————————————————
# Return only the rows where a specific column meets a condition (score >= 50).
def filter_data(rows):
    filtered = [row for row in rows if row["score"] >= 50.0]
    print(f"Filtered {len(filtered)} records matching the condition (score >= 50).")
    return filtered

# — Step 6 & 7: Sort and Save Results ————————————————————————————————
def save_sorted_results(rows, filepath):
    if not rows:
        print("No data to save.")
        return
    
    # Sort data by score descending
    sorted_data = sorted(rows, key=lambda x: x["score"], reverse=True)
    fieldnames = ["name", "department", "score"]
    
    try:
        with open(filepath, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(sorted_data)
        print(f"Sorted results successfully saved to {filepath}.")
    except IOError:
        print("Error: Could not write to output file.")

def main():
    data = load_data(INPUT_FILE)
    if data:
        print_summary(data)
        filtered_results = filter_data(data)
        save_sorted_results(filtered_results, OUTPUT_FILE)

if __name__ == "__main__":
    main()