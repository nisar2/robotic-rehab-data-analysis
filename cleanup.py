import os

def remove_mp4_files(directory):
    """
    Removes all .mp4 files from the specified directory and its subdirectories.

    Args:
        directory (str): The path to the directory to clean up.
    """
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.mp4'):
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                    print(f"Deleted: {file_path}")
                except Exception as e:
                    print(f"Failed to delete {file_path}: {e}")

if __name__ == "__main__":
    # Replace 'your_directory_path' with the path to the directory you want to clean up
    directory_to_clean = "/Users/harris/projects/robotic-rehab-data-analysis"
    if os.path.isdir(directory_to_clean):
        remove_mp4_files(directory_to_clean)
    else:
        print(f"The path '{directory_to_clean}' is not a valid directory.")