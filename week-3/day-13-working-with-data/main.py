# Day 13 — Working With Data
# Task: Load a CSV, manipulate lists and dicts, clean data, and print a summary.
# Submit this script along with your original CSV and the output CSV.

import csv

INPUT_FILE = "data/sample.csv"
OUTPUT_FILE = "data/output.csv"


# ── Step 1: Load CSV ──────────────────────────────────────────────────────────
# Open the CSV file using csv.DictReader and read each row into a list of dicts.

import csv

INPUT_FILE = "data/sample.csv"

# Step 1: Load CSV
def load_data(filepath):
    rows = []
    with open(filepath, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Clean string fields and convert score to integer
            row["name"] = row["name"].strip()
            row["score"] = int(row["score"])
            row["grade"] = row["grade"].strip()
            rows.append(row)
    return rows

# Test Step 1:
data = load_data(INPUT_FILE)
print("Loaded", len(data), "rows.")


# ── Step 2: Print Summary ─────────────────────────────────────────────────────
# Print the total number of rows.
# For any numeric column, print the minimum, maximum, and average values.

# Step 2: Print Summary
def print_summary(rows):
    # Collect all scores into a simple list
    scores = []
    for row in rows:
        scores.append(row["score"])
    
    total_count = len(scores)
    min_score = min(scores)
    max_score = max(scores)
    avg_score = sum(scores) / total_count
    
    print("--- DATA SUMMARY ---")
    print("Total Records:", total_count)
    print("Minimum Score:", min_score)
    print("Maximum Score:", max_score)
    print("Average Score:", round(avg_score, 2))

# Test Step 2:
print_summary(data)


# ── Step 3: Filter Data ───────────────────────────────────────────────────────
# Return only the rows where a specific column meets a condition.
# Example: score above 70, or price below 50.

# Step 3: Filter Data
def filter_data(rows):
    filtered = []
    for row in rows:
        # Keep only students who passed (score >= 70 or grade 'A')
        if row["score"] >= 70:
            filtered.append(row)
    return filtered


# ── Step 4: Sort and Export ───────────────────────────────────────────────────
# Sort the filtered data by one column and write the result to OUTPUT_FILE.

def save_data(rows, filepath):
   # Step 4: Save Filtered Data
   def save_data(filepath, rows):
    if len(rows) == 0:
        return

    fieldnames = list(rows[0].keys())
    with open(filepath, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    print("Saved", len(rows), "filtered rows to", filepath)


# --- Run All Steps ---
# 1. Load data
data = load_data(INPUT_FILE)

# 2. Print summary
print_summary(data)

# 3. Filter data
filtered_data = filter_data(data)

# 4. Save results to output CSV
save_data(OUTPUT_FILE, filtered_data)

# ── Main ──────────────────────────────────────────────────────────────────────
# --- Main Execution ---
if __name__ == "__main__":
    rows = load_data(INPUT_FILE)
    print_summary(rows)
    
    filtered = filter_data(rows)
    save_data(OUTPUT_FILE, filtered)