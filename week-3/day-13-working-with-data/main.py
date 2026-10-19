# Day 13 — Working With Data
# Task: Load a CSV, manipulate lists and dicts, clean data, and print a summary.
# Submit this script along with your original CSV and the output CSV.

import csv

# Exercise 2 - Read Dataset
def read_dataset(file_path):
    with open(file_path, mode='r', encoding='utf-8') as file:
        return list(csv.DictReader(file))
    

# Exercise 3 - Clean and Convert Data
def clean_data(records):
    return[
        {
            'Name': row['Name'].strip().lower().title(),
            'Score': float(row['Score'].strip()),
            'Department': row['Department'].strip().lower().title()
        }
        for row in records
    ]


# Exercise 4 - Analyse Dataset
def analyze_dataset(records):
    scores = [row['Score'] for row in records]
    print("== DATA SUMMARY ==")
    print(f"Total Records : {len(scores)}")
    print(f"Minimum Score : {min(scores)}")
    print(f"Maximum Score : {max(scores)}")
    print(f"Average Score : {sum(scores) / len(scores):.2f}")


# Exercise 5 - Filter Records
def filter_records(records, min_score=50):
    filtered = [row for row in records if row['Score'] >= min_score]
    print(f"\n=== PASSING STUDENTS (Score >= {min_score}) ===")
    for r in filtered:
        print(f"{r['Name']} - Score: {r['Score']} ({r['Department']})")
    return filtered

# Exercise 6 - Sort and Save Results
def save_sorted_results(records, output_file):
    sorted_records = sorted(records, key=lambda x: x['Score'], reverse=True)
    with open(output_file, mode='w', newline='',encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['Name', 'Score', 'Department'])
        writer.writeheader()
        writer.writerows(sorted_records)
    print(f"\nSaved {len(sorted_records)} records to '{output_file}'.")
    
# Exercise 7 - Main Execution
def main():
    cleaned_data = clean_data(read_dataset('data/sample.csv'))
    analyze_dataset(cleaned_data)
    passing = filter_records(cleaned_data, min_score=50)
    save_sorted_results(passing, 'passed_students_sorted.csv')


if __name__ == "__main__":
    main()


