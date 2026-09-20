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
