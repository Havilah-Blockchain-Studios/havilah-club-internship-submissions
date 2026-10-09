# Day 15 — Python Automation Project
# Choose one project type and implement it here:
#
#   A) File Organiser  — scans a folder and moves files into subfolders by extension
#   B) Report Generator — reads a CSV and produces a formatted text summary
#   C) Data Cleaner    — removes duplicate rows, strips whitespace, standardises columns
#
# Submit the complete project (this file + data folder + README.md) to GitHub.

import os
import shutil    # uncomment if using File Organiser

# Configuration
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_PATH = os.path.join(BASE_DIR, "data")
OUTPUT_PATH = os.path.join(BASE_DIR, "data", "output")


# — Core Functions —
# Break your project into small, clearly named functions.
def process(input_path, output_path):
    # Ensure input and output directories exist
    os.makedirs(input_path, exist_ok=True)
    os.makedirs(output_path, exist_ok=True)
    
    # Get absolute paths to avoid moving output into itself
    abs_output = os.path.abspath(output_path)
    
    # Loop through all items in the input folder
    for item in os.listdir(input_path):
        item_path = os.path.join(input_path, item)
        abs_file = os.path.abspath(item_path)
        
        # Skip subdirectories (including the output folder itself)
        if os.path.isdir(item_path) or abs_file.startswith(abs_output):
            continue
            
        # Extract extension without the dot (e.g., 'jpg', '.txt')
        _, ext = os.path.splitext(item)
        folder_name = ext.lstrip(".").lower() or "others"
        
        # Create extension target folder (e.g., data/output/pdf/)
        target_dir = os.path.join(output_path, folder_name)
        os.makedirs(target_dir, exist_ok=True)
        
        # Move file to its corresponding subfolder
        shutil.move(item_path, os.path.join(target_dir, item))


# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    print("Starting automation...")
    process(INPUT_PATH, OUTPUT_PATH)
    print("Done.")


if __name__ == "__main__":
    main()
