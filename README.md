
# Ommo HDF5 Data Processing Project

This project processes `.hdf5` files logged from Ommo's tracking system. It extracts 3D position data, computes average positions and maximum Euclidean distances for each sensor, and outputs the results into CSV files.

---

## Features

- Processes `.hdf5` files containing position data for sensors.
- Computes:
  - **Average X, Y, Z positions** for each sensor.
  - **Maximum Euclidean distance** for each sensor.
- Handles invalid `.hdf5` files and missing datasets gracefully.
- Generates two output CSV files:
  - `average_positions.csv`
  - `max_distances.csv`.
- Modular and tested design for reliability.

---

## Requirements

- Python 3.10 or later.
- Virtual environment (recommended) for dependency isolation.
- Dependencies:
  - `numpy`
  - `h5py`
  - `pytest` (for testing).

---

## Setup Instructions (A-Z)

### **1. Clone the Repository**
Clone the project repository to your local system:
```bash
git clone <repository_url>
cd OmmoProject
```

---

### **2. Create a Virtual Environment**
Create and activate a virtual environment for the project to avoid dependency conflicts:
```bash
python -m venv env
```

**On Windows:**
```bash
.\env\Scripts\activate
```

**On macOS/Linux:**
```bash
source env/bin/activate
```

---

### **3. Install Dependencies**
Install the required dependencies:
```bash
pip install -r requirements.txt
```

---

### **4. Prepare Input Data**
- Place your `.hdf5` files in a folder (e.g., `C:\path\to\input_folder`).
- Create an output folder where the results will be saved (e.g., `C:\path\to\output_folder`).

---

### **5. Run the Program**
Run the program using:
```bash
python main.py <input_folder_path> <output_folder_path>
```

**Example:**
```bash
python main.py C:\path\to\input_folder C:\path\to\output_folder
```

---

### **6. Verify Outputs**
After the program runs, you will find two CSV files in the specified output folder:
1. **`average_positions.csv`**:
   - Contains average X, Y, Z positions for each sensor.
   - Example:
     ```
     File Name,Sensor,Average X,Average Y,Average Z
     1.hdf5,Device_123_Sensor_0,0.123,0.456,0.789
     1.hdf5,Device_123_Sensor_1,0.987,0.654,0.321
     ```

2. **`max_distances.csv`**:
   - Contains maximum Euclidean distances for each sensor.
   - Example:
     ```
     File Name,Sensor,Max Distance
     1.hdf5,Device_123_Sensor_0,12.34
     1.hdf5,Device_123_Sensor_1,15.67
     ```

---

## Running Tests

Unit tests are included to ensure the program works as expected. To run the tests:
```bash
pytest tests/
```

You should see all tests pass:
```
============================= test session starts =============================
collected 4 items                                                              

tests/test_process.py ..                                                [  50%]
tests/test_utils.py ..                                                  [100%]

============================== 4 passed in 0.05s ==============================
```

---

## Project Structure

```
OmmoProject/
├── main.py                # Entry point for the program
├── process.py             # Core processing logic
├── utils.py               # Folder validation utilities
├── tests/                 # Unit tests
│   ├── test_process.py    # Tests for process.py
│   ├── test_utils.py      # Tests for utils.py
├── requirements.txt       # List of dependencies
├── README.md              # Project documentation
├── env/                   # Virtual environment (excluded from version control)
```

---

## Notes

- Invalid `.hdf5` files are skipped with appropriate warnings.
- Ensure the `Position` dataset exists in your `.hdf5` files; otherwise, it will be logged as missing.

---

## Authors

- **Hassan Mustafa** – Developer



