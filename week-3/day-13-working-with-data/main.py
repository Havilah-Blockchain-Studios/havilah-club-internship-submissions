# Day 13 — Working With Data
# Task: Load a CSV, manipulate lists and dicts, clean data, and print a summary.
# Submit this script along with your original CSV and the output CSV.


import csv

INPUT_FILE = "data/Students.csv"
OUTPUT_FILE = "data/output.csv"


# ── Step 1: Load CSV ──────────────────────────────────────────────────────────
# Open the CSV file using csv.DictReader and read each row into a list of dicts.

def load_data(filepath):
    rows = []
    # TODO: open the file and read rows into the list


    with open(filepath,"r", newline="",  encoding="utf-8") as file:
        reader =csv.DictReader(file)
        
        
        for row in reader:
            row["Score"] = float(row["Score"])
            row["Name"] = row["Name"].strip()
            row["Department"] = row["Department"].strip()

            rows.append(row)
            
            
    return rows
        
        

# ── Step 2: Print Summary ─────────────────────────────────────────────────────
# Print the total number of rows.
# For any numeric column, print the minimum, maximum, and average values.

def print_summary(rows):
    # TODO: implement summary statistics
    pass
    total_records = len(rows)


    print("--- DATA SUMMARY ---")
    print(f"Total records: {total_records}")

    if total_records > 0:
        scores = [row["Score"] for row in rows]
    
    
        min_score = min(scores)
        max_score = max(scores)
        average_score = sum(scores) / total_records

        print(f"Minimum score: {min_score}")
        print(f"Maximum score: {max_score}")
        print(f"Average score: {average_score:.2f}")
    
    
# ── Step 3: Filter Data ───────────────────────────────────────────────────────
# Return only the rows where a specific column meets a condition.
# Example: score above 70, or price below 50.

def filter_data(rows):
    filtered = []
    
    
    for row in rows:
        if row["Score"] >= 70:
            filtered.append(row)
            
    # TODO: define and apply your filter condition
    return filtered


# ── Step 4: Sort and Export ───────────────────────────────────────────────────
# Sort the filtered data by one column and write the result to OUTPUT_FILE.

def save_data(rows, filepath):
    # TODO: sort rows by a column, then write to CSV
    pass
    rows.sort(key=lambda row: row["Score"], reverse=True)
    
    with open(filepath, "w", newline="",) as file:
        
        fieldnames = ["Name", "Score", "Department"]
        
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(rows)
    
    
# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    rows = load_data(INPUT_FILE)
    
    print("ROWS LOADED:")
    for row in rows:
        print(row)
    
    print_summary(rows)
    
    filtered = filter_data(rows)
    
    save_data(filtered, OUTPUT_FILE)
    
    print(f"Done. {len(filtered)} rows written to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
