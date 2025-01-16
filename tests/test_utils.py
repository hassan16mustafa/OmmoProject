import sys
import os
import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils import validate_folder


def test_validate_existing_folder(tmp_path):
    """Test that validate_folder works for an existing folder."""
    validate_folder(str(tmp_path), "input")  # Should not raise an exception

def test_validate_nonexistent_folder():
    """Test that validate_folder raises an exception for a nonexistent folder."""
    with pytest.raises(SystemExit):
        validate_folder("nonexistent_folder", "input")
