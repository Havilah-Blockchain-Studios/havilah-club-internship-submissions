# Day 15 — Python Automation Project
# Project: Report Generator

import os
import csv

INPUT_PATH = "data/scores.csv"
OUTPUT_PATH = "data/report.txt"


def read_scores(input_path):
    records = []

    try:
        with open(input_path, "r", newline="") as file:
            reader = csv.DictReader(file)

            if not reader.fieldnames or "Name" not in reader.fieldnames or "Score" not in reader.fieldnames:
                print("Error: CSV must have Name and Score columns.")
                return []

            for row in reader:
                if row["Name"].strip() == "" or row["Score"].strip() == "":
                    continue

                try:
                    score = float(row["Score"])
                    records.append({
                        "Name": row["Name"].strip(),
                        "Score": score
                    })
                except ValueError:
                    print("Skipping a record with an invalid score.")

    except FileNotFoundError:
        print("Error: Input file was not found.")

    return records


def calculate_report(records):
    if not records:
        return None

    scores = [record["Score"] for record in records]

    report = {
        "count": len(records),
        "average": sum(scores) / len(scores),
        "highest": max(scores),
        "lowest": min(scores)
    }

    return report


def write_report(report, output_path):
    if report is None:
        print("No data to write.")
        return

    try:
        with open(output_path, "w") as file:
            file.write("STUDENT SCORE REPORT\n")
            file.write("====================\n")
            file.write(f"Number of records: {report['count']}\n")
            file.write(f"Average score: {report['average']:.2f}\n")
            file.write(f"Highest score: {report['highest']}\n")
            file.write(f"Lowest score: {report['lowest']}\n")

        print("Report created successfully.")

    except OSError as error:
        print("Error writing report:", error)


def process(input_path, output_path):
    records = read_scores(input_path)
    report = calculate_report(records)
    write_report(report, output_path)


def main():
    print("Starting automation...")
    process(INPUT_PATH, OUTPUT_PATH)
    print("Done.")


if __name__ == "__main__":
    main()