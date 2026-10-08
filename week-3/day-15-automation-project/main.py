# Day 15 - Python Automation Project
# Option A: File Organiser

import os
import shutil

# -- Configuration -----------------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_PATH = os.path.join(BASE_DIR, "data")
OUTPUT_PATH = INPUT_PATH

# -- Core Functions ----------------------------------------------------------

def check_directory(path):
    """Checks if the input directory exists and contains files."""
    if not os.path.exists(path):
        print(f"Error: Directory '{path}' does not exist.")
        return False
    if not os.listdir(path):
        print(f"Notice: Directory '{path}' is empty.")
        return False
    return True


def get_category(filename):
    """Determines target category subfolder based on file extension."""
    _, ext = os.path.splitext(filename)
    ext = ext.lower().replace('.', '')
    
    # Edge Case: Files without extensions
    if not ext:
        return "Others"
        
    categories = {
        "Documents": ["pdf", "txt", "docx", "xlsx"],
        "Images": ["png", "jpg", "jpeg", "gif"],
        "Archives": ["zip", "tar", "gz"],
        "Code": ["py", "js", "html", "css"]
    }
    
    for category, extensions in categories.items():
        if ext in extensions:
            return category
            
    return "Others"


def process(input_path, output_path):
    """Scans the folder and organizes files into categorized subfolders."""
    if not check_directory(input_path):
        return

    for filename in os.listdir(input_path):
        source_path = os.path.join(input_path, filename)

        # Skip subdirectories
        if os.path.isdir(source_path):
            continue

        category = get_category(filename)
        target_folder = os.path.join(input_path, category)

        try:
            os.makedirs(target_folder, exist_ok=True)
            shutil.move(source_path, os.path.join(target_folder, filename))
            print(f"Moved: {filename} -> {category}/")
        except Exception as e:
            print(f"Error moving {filename}: {e}")


# -- Main --------------------------------------------------------------------
def main():
    print("Starting automation...")
    process(INPUT_PATH, OUTPUT_PATH)
    print("Done.")


if __name__ == "__main__":
    main()