import os
import uuid

def rename_files_with_random_names(folder_path):
    # List all files in the folder
    files = os.listdir(folder_path)

    for file_name in files:
        # Generate a random name using UUID
        random_name = str(uuid.uuid4())

        # Get the file extension (if any)
        _, file_extension = os.path.splitext(file_name)

        # Construct the new file name
        new_file_name = random_name + file_extension.lower()

        # Build the full paths
        old_path = os.path.join(folder_path, file_name)
        new_path = os.path.join(folder_path, new_file_name)

        # Rename the file
        os.rename(old_path, new_path)
        print(f'Renamed: {file_name} -> {new_file_name}')

if __name__ == "__main__":
    folder_path = r""  # Replace with your folder path
    rename_files_with_random_names(folder_path)