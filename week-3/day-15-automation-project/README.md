Day 15 — Python Automation Project

Project: Report Generator

This project is a Python automation tool that reads student scores from a CSV file, processes the data, and creates a simple score report.

Requirements

- Python 3
- Python standard library ("csv")

How It Works

Input → Process → Output

1. Read student names and scores from "data/scores.csv".
2. Check that the CSV has the required columns.
3. Clean the names and convert scores to numbers.
4. Calculate:
   - Number of records
   - Average score
   - Highest score
   - Lowest score
5. Save the results in "data/report.txt".

How to Run

Open the terminal in the Day 15 project folder and run:

python main.py

Expected Output

The program creates "data/report.txt" containing a report like:

STUDENT SCORE REPORT
====================
Number of records: 8
Average score: 77.38
Highest score: 93.0
Lowest score: 55.0

Edge Cases Tested

The program was tested for:

- Missing input file
- Invalid score values
- Blank values
- Missing required CSV columns

The program handles these cases without crashing.