# Day 13 — Working With Data

import csv

INPUT_FILE = "data/sample.csv"
OUTPUT_FILE = "data/output.csv"




def load_data(filepath):
    rows = []
    with open(filepath, mode = 'r', newline= '') as file:
        reader = csv.DictReader(file)
        for row in reader:
            rows.append(row)
    return rows




def print_summary(rows):
    print("Total records:", len(rows))

    scores = [int(row["score"])for row in rows]

    print("Minimum score:", min(scores))
    print("Maximum score:", max(scores))
    print("Average score:", sum(scores) / len(scores))




def filter_data(rows):
    filtered = []
    for row in rows:
        if int(row["score"]) > 70:
            filtered.append(row)
    return filtered



def save_data(rows, filepath):
    sorted_rows = sorted(rows, key=lambda row: int(row["score"]))

    with open(filepath, mode= 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames = ["name", "score", "grade"])
        writer.writeheader()
        writer.writerows(sorted_rows)
    



def main():
    rows = load_data(INPUT_FILE)
    print_summary(rows)
    filtered = filter_data(rows)
    save_data(filtered, OUTPUT_FILE)
    print(f"Done. {len(filtered)} rows written to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
