    # Day 13 — Working With Data
    # Task: Load a CSV, manipulate lists and dicts, clean data, and print a summary.
    # Submit this script along with your original CSV and the output CSV.


    # ── Step 1: Load CSV ──────────────────────────────────────────────────────────
    # Open the CSV file using csv.DictReader and read each row into a list of dicts.
    
    
    
import csv
def load_data(filepath):
        rows = []
        with open(filepath, "r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                rows.append(row)
            return rows



    # ── Step 3: clean data ───────────────────────────────────────────────────────

def clean_data(rows):
    for row in rows:
        row["Price"] = float(row["Price"].replace("N", ""))
        row["Quantity"] = int(row["Quantity"])
    return rows
rows=load_data("C:\\Users\\chidi\\Downloads\\Day 13 task - task (1).csv")
cleaned_rows = clean_data(rows)
print(cleaned_rows)

    # ── Step 4: Analyze Data 
def print_summary(rows):
    total_records = len(rows)

    prices = [row["Price"] for row in rows]
    min_price = min(prices)
    max_price = max(prices)
    avg_price = sum(prices) / len(prices)

    print(f"Total records: {total_records}")
    print(f"Minimum Price: {min_price}")
    print(f"Maximum Price: {max_price}")
    print(f"Average Price: {avg_price:.2f}")

rows = load_data("C:\\Users\\chidi\\Downloads\\Day 13 task - task (1).csv")
cleaned_rows = clean_data(rows)
print_summary(cleaned_rows)

    #Filter data
    
def filter_data(cleaned_rows):
    filtered =[]
    for row in cleaned_rows:
        if row["Price"] > 15000:
            filtered.append(row)
    return filtered
filtered_rows = filter_data(cleaned_rows)
print("\nproducts with Price greater than 15000:")
for row in filtered_rows:
    print(row)
    
    
    #sort and save data
def save_data(rows, filepath):
    sorted_rows = sorted(rows, key=lambda row: row["Price"], reverse=True)
    with open(filepath, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["Product", "Price", "Quantity"])
        writer.writeheader()
        writer.writerows(sorted_rows)
Google_Drive = "week-3/day-13-working-with-data/data/output.csv"
output_filepath = Google_Drive
save_data(filtered_rows, output_filepath)
print("\nData saved to Google_Drive")