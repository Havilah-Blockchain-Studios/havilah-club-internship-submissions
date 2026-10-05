# Day 15 — Python Automation Project

## What does this project do?

A Python program that reads a CSV file of names and scores and produces a formatted text report. The report is printed on screen and saved to data/output/report.txt.


## Project Type

Report Generator

## Requirements

- Python 3
- No extra libraries needed (uses the built-in csv and os modules)
- A CSV file at data/scores.csv with name and score columns


## How to run

1. Open a terminal in the day-15-automation-project folder.
2. Run:
  
   python main.py
   

## Example output

Starting automation...
==============================
     SCORE REPORT
==============================
Number of records : 8
Average score     : 78.25
Highest score     : 95
Lowest score      : 54
==============================
Report saved to .../data/output/report.txt

## Edge Cases Handled

- Missing input file: prints a clear error and stops
- Empty file or missing score column: prints an error and stops
- Blank or non-number scores: skipped, with a note showing how man
