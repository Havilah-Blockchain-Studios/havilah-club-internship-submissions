# Day 15 — Python Automation Project

## What does this project do?

This project automates the parsing and statistical analysis of student performance records stored in CSV files. It eliminates manual data calculation by automatically filtering out missing or corrupted entries, computing key statistics (total count, average score, maximum, and minimum scores), and outputting a formatted text report.

## Project Type

Report Generator

## Requirements

No external libraries are required. The script relies strictly on Python standard library modules (`csv` and `os`).

## How to run

```bash
python main.py

## Example Output
========================================
        STUDENT PERFORMANCE REPORT      
========================================
Total Valid Records Analyzed : 10
Average Score                : 77.25
Highest Score                : 95.0 (Tunde Bakare, Victor Chukwudi)
Lowest Score                 : 45.0 (Blessing Egbe)
========================================

Report successfully generated at: data/output/report.txt