import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from process import calculate_averages, calculate_max_distance


def test_calculate_averages():
    """Test average calculation for a sensor."""
    sensor_data = np.array([
        [1.0, 2.0, 3.0],
        [4.0, 5.0, 6.0],
        [7.0, 8.0, 9.0]
    ])  # 3 samples with x, y, z coordinates

    avg_x, avg_y, avg_z = calculate_averages(sensor_data)
    assert avg_x == 4.0
    assert avg_y == 5.0
    assert avg_z == 6.0

def test_calculate_max_distance():
    """Test max distance calculation for a sensor."""
    sensor_data = np.array([
        [1.0, 2.0, 2.0],  # Distance = sqrt(1^2 + 2^2 + 2^2) = 3.0
        [3.0, 6.0, 2.0],  # Distance = sqrt(3^2 + 6^2 + 2^2) = 7.0
        [2.0, 2.0, 1.0]   # Distance = sqrt(2^2 + 2^2 + 1^2) = 3.0
    ])

    max_distance = calculate_max_distance(sensor_data)
    assert max_distance == 7.0

def test_calculate_averages_empty_dataset():
    """Test average calculation with an empty dataset."""
    sensor_data = np.empty((0, 3))  # No samples
    avg_x, avg_y, avg_z = calculate_averages(sensor_data)
    assert avg_x == 0.0
    assert avg_y == 0.0
    assert avg_z == 0.0


def test_calculate_averages_single_sample():
    """Test average calculation with a single sample."""
    sensor_data = np.array([[1.0, 2.0, 3.0]])
    avg_x, avg_y, avg_z = calculate_averages(sensor_data)
    assert avg_x == 1.0
    assert avg_y == 2.0
    assert avg_z == 3.0

def test_calculate_max_distance_empty_dataset():
    """Test max distance calculation with an empty dataset."""
    sensor_data = np.empty((0, 3))  # No samples
    max_distance = calculate_max_distance(sensor_data)
    assert max_distance == 0.0
