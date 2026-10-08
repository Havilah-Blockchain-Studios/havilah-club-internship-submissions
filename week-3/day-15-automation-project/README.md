# Day 15 — Python Automation Project

## What does this project do?

This project automates the process of reading and parsing student data from a raw CSV file. It calculates key class-wide metrics such as the total number of student records, the average class score, and identifies the highest and lowest scoring individuals. The final results are automatically structured and saved as a polished text report while also outputting a live copy directly to the terminal

## Project Type

Report Generator

## Requirements

# No external libraries needed
# Standard library imports: os, csv


## How to run

```bash
python week-3/day-15-automation-project/main.py
```

## Example output

Starting automation...
Reading input data from: week-3/day-15-automation-project/data/scores.csv...
Analyzing data and aggregating metrics...
Writing final summary out to: week-3/day-15-automation-project/data/output/report.txt...

==================================================
        STUDENT PERFORMANCE AUTOMATED REPORT          
==================================================
Total Records Processed : 25
Average Class Score     : 82.45
--------------------------------------------------
Highest Score Achieved  : 99 (Alice Smith)
Lowest Score Achieved   : 54 (Bob Jones)
==================================================
Report generated automatically by Day 15 Engine.

Done.
