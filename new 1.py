import os

def convert_filenames_to_uppercase(root_folder):
    for folder_path, _, files in os.walk(root_folder):
        # Rename files
        for file_name in files:
            name, extension = os.path.splitext(file_name)
            old_path = os.path.join(folder_path, file_name)
            new_file_name = name.upper() + extension.lower()
            new_path = os.path.join(folder_path, new_file_name)
            os.rename(old_path, new_path)
            print(f'Renamed: {file_name} -> {new_file_name}')

        # Rename folders
        for subfolder_name in _:
            old_path = os.path.join(folder_path, subfolder_name)
            new_folder_name = subfolder_name.upper()
            new_path = os.path.join(folder_path, new_folder_name)
            os.rename(old_path, new_path)
            print(f'Renamed folder: {subfolder_name} -> {new_folder_name}')

if __name__ == "__main__":
    root_folder = r""  # Replace with your root folder path
    convert_filenames_to_uppercase(root_folder)
