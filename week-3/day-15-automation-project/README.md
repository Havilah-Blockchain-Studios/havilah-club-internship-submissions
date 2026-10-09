# Day 15: Python Automation Project (Report Generator)

## Project description
A small Python tool that reads a CSV file of names and scores and produces a
formatted text report. The report shows the number of records, the average
score, the highest score and the lowest score. It is printed to the screen and
saved to a file.

## Plan
- **Input:** `data/scores.csv`, with at least the columns `name` and `score`
- **Process:** read the rows, convert each score to a number, then calculate
  the count, average, highest and lowest
- **Output:** a text report printed to the screen and saved to
  `data/output/report.txt`
- **Edge cases:** missing input file, missing columns, blank or invalid scores,
  empty file

## Project structure
```
main.py            the program
data/scores.csv    the input data (10 records)
data/output/       the report is saved here when the program runs
README.md          this file
```

## Requirements
- Python 3
- No extra packages. It uses only the standard library (`os` and `csv`).

## How to run
Run the program from inside the project folder, because the file paths are
relative:
```
cd week-3/day-15-automation-project
python main.py
```

## Example output
```
Starting automation...
==============================
SCORE REPORT
==============================
Number of records: 10
Average score: 77.4
Highest score: 94.0 (Ife)
Lowest score: 55.0 (Bola)
==============================
Done.
```

## Functions
- `read_scores`: reads the CSV and returns the records
- `calculate_stats`: works out the count, average, highest and lowest
- `build_report`: formats the results as text
- `save_report`: writes the report to a file
- `process`: runs the steps in order
- `main`: starts the program

## Edge cases tested
- **Missing input file:** when `data/scores.csv` could not be found (for
  example when the script was run from the wrong folder), the program printed
  a clear message instead of crashing:
```
  Error: could not find 'data/scores.csv'.
  Check the file exists and run this script from the Day 15 folder.
```
- **Missing column:** when a CSV had no `score` column, the program printed
  `Error: the CSV is missing the 'score' column.` and stopped cleanly.

## Also handled in the code (not separately tested)
- Rows with a blank or non-numeric score are skipped with a message.
- An empty CSV file, or one with no valid records, produces a message instead
  of a report.

## Note
Column names must match exactly. During testing, a test file whose header was
`   name,score` (with leading spaces) was reported as missing the `name`
column.