import os
from collections import defaultdict


def organize_files(source_folder):
    # Get sorted list of files
    files = sorted(
        [
            f
            for f in os.listdir(source_folder)
            if os.path.isfile(os.path.join(source_folder, f))
        ]
    )

    # Dictionary to hold grouped files by their common prefix (ignoring brackets and extensions)
    grouped_files = defaultdict(list)

    for file_name in files:
        # Extract base name without extension and brackets
        base_name = file_name.split("(")[0].strip()
        grouped_files[base_name].append(file_name)

    # Create folders and move files
    folder_index = 0
    current_folder_files = []
    for base_name, group in grouped_files.items():
        if len(current_folder_files) + len(group) > 200:
            # Create a new folder
            start_name = current_folder_files[0][:2].lower()
            end_name = current_folder_files[-1][:2].lower()
            folder_name = f"from_{start_name}_to_{end_name}"
            folder_path = os.path.join(source_folder, folder_name)
            os.makedirs(folder_path, exist_ok=True)

            # Move files to the folder
            for file_name in current_folder_files:
                src_path = os.path.join(source_folder, file_name)
                dest_path = os.path.join(folder_path, file_name)
                os.rename(src_path, dest_path)

            # Reset current folder
            current_folder_files = []

        # Add group to current folder
        current_folder_files.extend(group)

    # Handle remaining files
    if current_folder_files:
        start_name = current_folder_files[0][:2].lower()
        end_name = current_folder_files[-1][:2].lower()
        folder_name = f"from_{start_name}_to_{end_name}"
        folder_path = os.path.join(source_folder, folder_name)
        os.makedirs(folder_path, exist_ok=True)

        for file_name in current_folder_files:
            src_path = os.path.join(source_folder, file_name)
            dest_path = os.path.join(folder_path, file_name)
            os.rename(src_path, dest_path)


if __name__ == "__main__":
    source_folder = "Folder contains ZX Files"
    source_subFolder = "Subfolder contains games"
    organize_files(source_folder + "/" + source_subFolder)
    print("Files organized successfully!")
