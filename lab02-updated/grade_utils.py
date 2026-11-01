"""TODO: describe what this module is for."""
"""Utilities for converting GPA scores to letter grades on a 5.00 scale."""

def letter_grade(gpa):
    """TODO: describe what this function does."""
    # TODO: your if/elif chain here
    """Return letter grade for given GPA."""
    if gpa >= 4.50:
        return "A"
    elif gpa >= 3.50:
        return "B"
    elif gpa >= 2.50:
        return "C"
    elif gpa >= 1.50:
        return "D"
    else:
        return "F"
