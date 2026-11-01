"""TODO: describe this module."""
"""Utility functions for processing and cleaning text data."""

def clean_name(raw):
    """TODO: describe this function."""
    # TODO: collapse whitespace, then title-case
    """Clean a name string by removing extra whitespace and capitalizing words."""
    cleaned = " ".join(raw.split())
    return cleaned.title()
