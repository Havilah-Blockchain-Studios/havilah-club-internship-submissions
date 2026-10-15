# Day 15 — Python Automation Project

import os
import shutil  


INPUT_PATH = "data/"
OUTPUT_PATH = "data/output/"


def process(input_path, output_path):
    files = os.listdir(input_path)
    for filename in files:
        full_path = os.path.join(input_path, filename)
        if os.path.isfile(full_path):
            extension = os.path.splitext(filename)[1].replace(".", "")
            if extension == "":
                extension = "no_extension"
            folder_path = os.path.join(output_path, extension)
            os.makedirs(folder_path, exist_ok = True)
            shutil.move(full_path, os.path.join(folder_path, filename))


    


# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    print("Starting automation...")
    process(INPUT_PATH, OUTPUT_PATH)
    print("Done.")


if __name__ == "__main__":
    main()
