import os
import sys

def validate_folder(folder_path, folder_type):
    """Validates the existence of a folder."""
    if not os.path.isdir(folder_path):
        print(f"Error: {folder_type.capitalize()} folder '{folder_path}' does not exist.")
        sys.exit(1)
