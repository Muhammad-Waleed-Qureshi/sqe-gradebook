import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

import pytest
from gradebook.gradebook import validate_name


def test_valid_typical_name():
    assert validate_name("Ali Khan") == "Ali Khan"


@pytest.mark.parametrize("bad", [
    "",
    "A" * 51,
    "Ali123",
    "Ali@Khan",
])
def test_invalid_names(bad):
    with pytest.raises(ValueError):
        validate_name(bad)




# ---------- Lab 6: Boundary tests for validate_name ----------
# Rule: length 1–50 (after strip), letters/spaces/hyphens only.

@pytest.mark.parametrize("name,should_pass", [
    ("", False),                # length 0 -> invalid
    ("A", True),                # length 1 (min)
    ("A" + "b" * 48, True),     # length 49 (max-1)
    ("A" + "b" * 49, True),     # length 50 (max)
    ("A" + "b" * 50, False),    # length 51 (max+1) -> invalid
])
def test_validate_name_length_boundaries(name, should_pass):
    if should_pass:
        assert validate_name(name) == name.strip()
    else:
        with pytest.raises(ValueError):
            validate_name(name)
