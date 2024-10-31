import os

# Define the path to the folder and the allowed file extensions
FOLDER_PATH = "C:/Users/micha/Dota"  # Replace this with your target folder path
FILE_EXTENSIONS = ["cs"]

def count_lines(file_path):
    """Counts non-empty lines in a file."""
    line_count = 0
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        for line in file:
            #if line.strip():  # Only count non-empty lines
                line_count += 1
    return line_count

def process_folder(folder_path):
    """Recursively processes folders and counts lines in matching files."""
    total_line_count = 0
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            file_extension = file_name.split('.')[-1]
            if file_extension in FILE_EXTENSIONS:
                file_path = os.path.join(root, file_name)
                line_count = count_lines(file_path)
                print(f"{file_name} has {line_count} lines.")
                total_line_count += line_count
    print(f"Total non-empty lines in matching files: {total_line_count}")

# Run the function on the specified folder path
process_folder(FOLDER_PATH)
