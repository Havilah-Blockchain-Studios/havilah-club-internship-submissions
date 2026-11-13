# Day 15 — Python Automation Project

## What does this project do?

This project automates file management by scanning a messy folder, reading each file's extension, and automatically moving it into a corresponding subfolder. It saves time and keeps directories clean and organized

## Project Type

File Organiser

## Project Planning (Input → Process → Output → Edge Cases)
- **Input:** A folder named `data/` containing test files with various extensions
- **Process:** The script validates the folder path, loops through items, extracts file extensions, creates subfolders dynamically, and moves files using `shutil`
- **Output:** Neatly organized subfolders inside the data directory grouped by file extension
- **Edge Cases Handled:** 
  1. Missing input folder validation (prevents crashes)
  2. Skipping files without extensions (such as `.gitkeep`) safely

## Requirements

This project uses only Python's built-in standard libraries, so no extra installations are required

```
- `os`
- `shutil`

## How to run

```bash
python week-3/day-15-automation-project/main.py
```

## Example output

 Starting automation...
Skipped (no extension): .gitkeep
Moved: notes.txt -> txt/
Moved: picture.png -> png/
Moved: report.pdf -> pdf/
Moved: script.py -> py/
Moved: table.csv -> csv/
Automation finished successfully.


