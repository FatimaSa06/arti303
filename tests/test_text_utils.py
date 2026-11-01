"""Tests for src/text_utils.py"""
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

import text_utils


def test_clean_name_whitespace():
    """Verify that leading/trailing and excess internal whitespace is cleaned."""
    assert text_utils.clean_name("  Sara   Alotaibi  ") == "Sara Alotaibi"


def test_clean_name_capitalisation():
    """Verify that student names are formatted with proper title casing."""
    assert text_utils.clean_name("sara alotaibi") == "Sara Alotaibi"
