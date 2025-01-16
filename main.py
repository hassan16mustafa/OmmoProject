import argparse  # For handling command-line arguments
import os
from utils import validate_folder  # Import folder validation from utils.py
from process import process_files  # Import the processing logic from process.py

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Ommo HDF5 File Processor")
    parser.add_argument("input_folder", type=str, help="Folder containing HDF5 files")
    parser.add_argument("output_folder", type=str, help="Folder to save output CSV files")
    args = parser.parse_args()  # Parse the provided arguments

    # Validate input and output folders
    validate_folder(args.input_folder, "input")
    validate_folder(args.output_folder, "output")

    # Process the HDF5 files
    process_files(args.input_folder, args.output_folder)

if __name__ == "__main__":
    main()
