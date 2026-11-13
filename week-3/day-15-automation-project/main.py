# Day 15 - Python Automation Project
# Choose one project type and implement it here:
# A) File Organiser — scans a folder and moves files into subfolders by extension
# B) Report Generator — reads a CSV and produces a formatted text summary[cite: 11]
# C) Data Cleaner — removes duplicate rows, strips whitespace, standardises columns[cite: 11]
# Submit the complete project (this file + data folder + README.md) to GitHub.[cite: 11]

import os
import shutil  # uncomment if using File Organiser[cite: 9]
# import csv   # uncomment if using Report Generator or Data Cleaner[cite: 9]

# — Configuration —
# Set your input/output paths here so they are easy to find and change.[cite: 9]
INPUT_PATH = "week-3/day-15-automation-project/data/"
OUTPUT_PATH = "week-3/day-15-automation-project/data/"

# — Core Functions —
# Break your project into small, clearly named functions.[cite: 9]
# Each function should do one thing.[cite: 9]

def check_input_folder(path):
    """Edge Case 1: Check if the input folder actually exists."""
    if not os.path.exists(path):
        print(f"Error: The folder '{path}' does not exist.")
        return False
    return True

def organize_files(input_dir, output_dir):
    """Scans the folder and sorts files into subfolders by extension."""
    for file_name in os.listdir(input_dir):
        file_path = os.path.join(input_dir, file_name)
        
        # Skip if it's a directory, only process files
        if os.path.isdir(file_path):
            continue
            
        # Get file name and extension
        name, ext = os.path.splitext(file_name)
        
        # Edge Case 2: Skip files that have no extension
        if ext == "":
            print(f"Skipped (no extension): {file_name}")
            continue
            
        # Clean the extension name (e.g., '.txt' becomes 'txt')
        folder_name = ext[1:].lower()
        
        # Create subfolder inside output path if it doesn't exist
        dest_folder = os.path.join(output_dir, folder_name)
        if not os.path.exists(dest_folder):
            os.makedirs(dest_folder)
            
        # Move the file into its extension folder
        dest_path = os.path.join(dest_folder, file_name)
        shutil.move(file_path, dest_path)
        print(f"Moved: {file_name} -> {folder_name}/")

# — Main —
def main():
    print("Starting automation...")
    
    # Validate path before running
    if check_input_folder(INPUT_PATH):
        organize_files(INPUT_PATH, OUTPUT_PATH)
        print("Automation finished successfully.")
    else:
        print("Automation stopped.")

if __name__ == "__main__":
    main()