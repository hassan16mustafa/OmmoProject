import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from main import main

def test_integration_valid_data(tmp_path, monkeypatch):
    """Test the program with valid data."""
    # Simulate input and output folders
    input_folder = tmp_path / "input"
    input_folder.mkdir()
    output_folder = tmp_path / "output"
    output_folder.mkdir()

    # Create a sample HDF5 file
    import h5py
    sample_file = input_folder / "sample.hdf5"
    with h5py.File(sample_file, 'w') as f:
        group = f.create_group("Device_123")
        dataset = group.create_dataset("Position", data=[
            [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]],
            [[7.0, 8.0, 9.0], [10.0, 11.0, 12.0]]
        ])

    # Mock command-line arguments
    monkeypatch.setattr(sys, 'argv', ["main.py", str(input_folder), str(output_folder)])

    # Run the main function
    main()

    # Verify outputs
    assert (output_folder / "average_positions.csv").exists()
    assert (output_folder / "max_distances.csv").exists()