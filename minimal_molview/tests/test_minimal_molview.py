"""
Unit and regression test for the minimal_molview package.
"""

# Import package, test suite, and other packages as needed
import sys

import pytest

import minimal_molview


def test_minimal_molview_imported():
    """Sample test, will always pass so long as import statement worked."""
    assert "minimal_molview" in sys.modules
