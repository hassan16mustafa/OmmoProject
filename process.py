import os
import h5py
import numpy as np
import csv
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def extract_position_data(hdf, group):
    """Extracts the Position dataset for a given group."""
    if 'Position' in hdf[group]:
        logging.info(f" - Found 'Position' dataset in group: {group}")
        return hdf[group]['Position'][:]
    logging.warning(f" - No 'Position' dataset in group: {group}")
    return None

def calculate_averages(sensor_data):
    """Calculates the average X, Y, Z positions for a sensor."""
    avg_x = np.mean(sensor_data[:, 0])
    avg_y = np.mean(sensor_data[:, 1])
    avg_z = np.mean(sensor_data[:, 2])
    return avg_x, avg_y, avg_z

def calculate_max_distance(sensor_data):
    """Calculates the maximum Euclidean distance for a sensor."""
    distances = np.sqrt(np.sum(sensor_data**2, axis=1))  # Euclidean distance formula
    return np.max(distances)

def write_csv(file_path, data, headers):
    """Writes data to a CSV file."""
    logging.info(f"Writing data to CSV: {file_path}")
    with open(file_path, mode='w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(headers)
        csv_writer.writerows(data)

def process_files(input_folder, output_folder):
    """Processes HDF5 files in the input folder and calculates metrics."""
    # List all files in the input folder
    files = os.listdir(input_folder)
    hdf5_files = [file for file in files if file.endswith('.hdf5')]

    if not hdf5_files:
        logging.warning("No valid HDF5 files found in the input folder.")
        return

    logging.info(f"Found {len(hdf5_files)} HDF5 file(s).")

    avg_csv_data = []
    max_csv_data = []

    for file in hdf5_files:
        file_path = os.path.join(input_folder, file)
        try:
            with h5py.File(file_path, 'r') as hdf:
                logging.info(f"Processing file: {file}")

                groups = list(hdf.keys())
                for group in groups:
                    position_data = extract_position_data(hdf, group)
                    if position_data is not None:
                        logging.info(f"Position dataset shape: {position_data.shape}")

                        num_sensors = position_data.shape[1]
                        for sensor_idx in range(num_sensors):
                            sensor_data = position_data[:, sensor_idx, :]

                            # Calculate averages
                            avg_x, avg_y, avg_z = calculate_averages(sensor_data)
                            avg_csv_data.append([file, f"{group}_Sensor_{sensor_idx}", avg_x, avg_y, avg_z])

                            # Calculate maximum distance
                            max_distance = calculate_max_distance(sensor_data)
                            max_csv_data.append([file, f"{group}_Sensor_{sensor_idx}", max_distance])
        except Exception as e:
            logging.error(f"Error processing file {file}: {e}")

    # Write CSV files
    write_csv(
        os.path.join(output_folder, "average_positions.csv"),
        avg_csv_data,
        ["File Name", "Sensor", "Average X", "Average Y", "Average Z"]
    )
    write_csv(
        os.path.join(output_folder, "max_distances.csv"),
        max_csv_data,
        ["File Name", "Sensor", "Max Distance"]
    )

    logging.info("Processing complete! Results written to output folder.")
