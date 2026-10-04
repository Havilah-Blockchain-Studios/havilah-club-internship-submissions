# Day 15 - Automation Project: File Organiser
# Scans a folder and sorts its files into subfolders based on file extension.
#
# Plan (Input -> Process -> Output):
#   Input:   a folder path containing a mix of files
#   Process: read each file's extension, create a matching subfolder if
#            needed, and move the file into it
#   Output:  the same folder, now organised into extension-named subfolders
#
# Edge cases handled:
#   1. The input folder does not exist
#   2. The input folder is empty (nothing to organise)
#   3. A file has no extension (grouped into "no_extension")
#   4. A destination file with the same name already exists (renamed, not overwritten)

import os
import shutil

SOURCE_FOLDER = "test_folder"


def get_target_folder(filename):
    """Return the subfolder name a file should be moved into, based on its extension."""
    _, extension = os.path.splitext(filename)
    if extension == "":
        return "no_extension"
    return extension[1:].lower() + "_files"


def build_destination_path(folder_path, filename):
    """
    Return a safe destination path inside folder_path for filename.
    If a file with that name already exists there, add a number
    (e.g. notes_1.txt) instead of overwriting it.
    """
    destination = os.path.join(folder_path, filename)
    if not os.path.exists(destination):
        return destination

    name, extension = os.path.splitext(filename)
    counter = 1
    while True:
        new_name = f"{name}_{counter}{extension}"
        destination = os.path.join(folder_path, new_name)
        if not os.path.exists(destination):
            return destination
        counter += 1


def organise_folder(source_folder):
    """Scan source_folder and move each file into an extension-based subfolder."""
    if not os.path.isdir(source_folder):
        print(f"Error: the folder '{source_folder}' does not exist.")
        return

    entries = os.listdir(source_folder)
    files = [f for f in entries if os.path.isfile(os.path.join(source_folder, f))]

    if not files:
        print(f"'{source_folder}' has no files to organise.")
        return

    moved_count = 0
    for filename in files:
        source_path = os.path.join(source_folder, filename)
        target_folder_name = get_target_folder(filename)
        target_folder_path = os.path.join(source_folder, target_folder_name)

        os.makedirs(target_folder_path, exist_ok=True)

        destination_path = build_destination_path(target_folder_path, filename)
        shutil.move(source_path, destination_path)
        print(f"Moved: {filename} -> {target_folder_name}/")
        moved_count += 1

    print(f"\nDone. {moved_count} file(s) organised in '{source_folder}'.")


def main():
    organise_folder(SOURCE_FOLDER)


if __name__ == "__main__":
    main()
